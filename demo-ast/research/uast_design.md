# Thiết kế UAST (Unified Abstract Syntax Tree) cho Code Context System

Dựa trên mục tiêu của project là "Xây dựng hệ thống cung cấp context cho coding agent thông qua giao thức MCP" với các tính năng như parse code, lưu vào graph database và vector database, UAST cần được thiết kế để chuẩn hoá (normalize) cú pháp của nhiều ngôn ngữ khác nhau thành các khái niệm ngữ nghĩa chung (semantic concepts). Điều này giúp hệ thống (và Agent) xử lý code một cách đồng nhất, không phụ thuộc vào ngôn ngữ nguồn.

## 1. Các Tree-sitter Captures Cần Thiết
Tree-sitter sử dụng file `queries/tags.scm` (hoặc custom queries) để trích xuất thông tin. Để build UAST hoàn chỉnh, chúng ta cần map các capture mặc định và bổ sung thêm các capture tùy chỉnh:

### Code Navigation Captures (Cấu trúc chương trình)
- `@definition.class`, `@definition.interface`, `@definition.struct`, `@definition.enum`
- `@definition.function`, `@definition.method`
- `@definition.variable`, `@definition.constant`, `@definition.field`
- `@reference.call` (Rất quan trọng để build Call Graph - trace who calls who)
- `@reference.class`, `@reference.type` (Theo dõi data types và inheritance)

### Context & Semantics Captures (Ngữ cảnh)
- `@comment`, `@doc` (Docstrings, Javadoc, XML doc - cực kỳ quan trọng cho Vector Search)
- `@definition.import`, `@definition.export` (Theo dõi dependencies giữa các file/module)
- `@definition.parameter` (Xác định signature của hàm)
- `@annotation`, `@decorator` (Trích xuất các metadata liên quan tới Framework như API routes, DI injections)

---

## 2. Cấu trúc chung của UAST (Base Structure)

Vì server dự kiến viết bằng **Python** (FastAPI), chúng ta nên sử dụng `pydantic` để định nghĩa cấu trúc dữ liệu. UAST cần chứa đủ thông tin để:
1. Định vị được trong source code (báo lại cho IDE hoặc highlight)
2. Hiểu được ngữ nghĩa (phục vụ LLM)
3. Lưu trữ nguyên bản làm Node trong Graph Database (Neo4j) và embed vào Vector Database.

```python
from pydantic import BaseModel, Field
from typing import List, Optional, Any, Dict, Literal

class Position(BaseModel):
    row: int
    column: int

class UASTNode(BaseModel):
    # Định danh
    id: str = Field(..., description="UUID hoặc Hash (file_path + start_byte + end_byte) để làm ID unique trong GraphDB")
    node_type: str = Field(..., description="Loại node chung (class, function, variable, import, call, file)")
    language: str = Field(..., description="Ngôn ngữ nguồn (python, java, typescript...)")
    name: str = Field(..., description="Tên định danh của entity")
    
    # Vị trí trong source code (tương thích với định dạng của Tree-sitter)
    file_path: str
    start_point: Position
    end_point: Position
    start_byte: int
    end_byte: int
    
    # Dữ liệu phục vụ LLM (Vector DB)
    source_code: str = Field(..., description="Đoạn source code nguyên bản của node (dùng để chunking và embed)")
    docstring: Optional[str] = Field(default=None, description="Tài liệu/Comment gắn trực tiếp với node")
    
    # Quan hệ cấu trúc phân cấp (Hierarchy)
    children: List['UASTNode'] = Field(default_factory=list, description="Các node con (ví dụ: class chứa methods)")
    
    # Metadata mở rộng để xử lý edge cases của các ngôn ngữ
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Lưu trữ decorators, annotations, visibility...")
```

---

## 3. Implement Cấu trúc cho các Entity Cụ thể (Subclasses)

Dựa trên `UASTNode`, chúng ta kế thừa để tạo các node chuyên biệt.

### 3.1. File / Module Node
Là node gốc của mỗi file source code, đóng vai trò bao bọc tất cả các node khác.
```python
class FileNode(UASTNode):
    node_type: Literal["file"] = "file"
    imports: List['ImportNode'] = Field(default_factory=list)
```

### 3.2. Function / Method Node
```python
class FunctionNode(UASTNode):
    node_type: Literal["function", "method"] = "function"
    parameters: List[str] = Field(default_factory=list)
    return_type: Optional[str] = None
    is_async: bool = False
    modifiers: List[str] = Field(default_factory=list) # public, private, static, abstract
    
    # Call dependencies (Dùng để sau này tạo Edge [:CALLS] trong GraphDB)
    calls: List[str] = Field(default_factory=list, description="Tên hoặc ID của các hàm bị gọi bên trong hàm này")
```

### 3.3. Class / Interface / Trait Node
```python
class ClassNode(UASTNode):
    node_type: Literal["class", "interface", "struct", "trait", "enum"] = "class"
    base_classes: List[str] = Field(default_factory=list, description="Các class/interface kế thừa")
    modifiers: List[str] = Field(default_factory=list)
```

### 3.4. Variable / Field Node
```python
class VariableNode(UASTNode):
    node_type: Literal["variable", "field", "constant"] = "variable"
    data_type: Optional[str] = None
    is_global: bool = False
    value: Optional[str] = None # Giá trị khởi tạo (hữu ích cho hằng số)
```

### 3.5. Import Node (Dependency Tracking)
```python
class ImportNode(UASTNode):
    node_type: Literal["import"] = "import"
    module_source: str = Field(..., description="Đích import (vd: 'os', 'typing', './utils')")
    imported_names: List[str] = Field(default_factory=list, description="Tên các biến/hàm được import (hoặc alias)")
    is_wildcard: bool = False
```

---

## 4. Xử lý Edge Cases: Syntax đặc trưng của từng ngôn ngữ (Language-Specific Quirks)

Mỗi ngôn ngữ có các feature ngữ nghĩa không map 1-1 với cấu trúc UAST chuẩn. Cách giải quyết chung là xử lý riêng ở **người phân tích (Language Parser Adapter)** và lưu vào trường `metadata` hoặc chuẩn hoá.

### 4.1. Python: Decorators
- **Vấn đề**: Decorator (`@app.get('/path')`, `@classmethod`) mang khối lượng ngữ nghĩa cực lớn, xác định hành vi của hàm hoặc class.
- **Giải quyết**: Trích xuất decorator từ AST bằng capture `@decorator`. Adapter của Python sẽ gán danh sách này vào `metadata` của `FunctionNode`/`ClassNode`.
- **Ứng dụng**: GraphDB query có thể dễ dàng tìm ra tất cả "API Routes" bằng cách filter nodes có metadata chứa `@app.**.

### 4.2. Java/C#: Annotations
- **Vấn đề**: Tương tự Python, Annotations (`@Override`, `@Entity`, `@Autowired`) là xương sống của các framework.
- **Giải quyết**: Thêm capture `@annotation`. Lưu ý cần bóc tách các parameter của annotation (như tên bảng trong database `@Table(name="users")`) để đưa vào JSON cấu trúc lưu trong `metadata`.

### 4.3. JavaScript/TypeScript: Anonymous Functions và Arrow Functions
- **Vấn đề**: Khai báo bằng phép gán: `export const myFunc = async () => {}`. AST mặc định sẽ hiểu đây là một `VariableDeclaration` chứ không phải một `Function`.
- **Giải quyết**: Adapter của TS/JS cần xử lý look-ahead. Nếu giá trị khởi tạo của một biến là arrow function, tự động promote (nâng cấp) nó lên thành `FunctionNode`, với tên là tên của biến (`myFunc`). Lưu flag `is_exported: true` vào `metadata`.

### 4.4. Go: Structs và Receiver Methods
- **Vấn đề**: Go không có class từ khóa. Các phương thức được liên kết với struct thông qua syntax *receiver* ở bên ngoài block của struct: `func (s *MyStruct) DoSomething()`.
- **Giải quyết**: 
  - `struct` -> map thành `ClassNode`.
  - Adapter của Go khi duyệt tới các hàm có *receiver* sẽ trích xuất type của receiver (`MyStruct`).
  - Sau đó, Adapter tự động add hàm đó vào thuộc tính `children` của `ClassNode` tương ứng, giúp UAST cuối cùng trông giống hệt như các ngôn ngữ OOP tiêu chuẩn (Method nằm bên trong Class).

### 4.5. Rust: Traits, Impl Blocks, Macros
- **Vấn đề**: Rust định nghĩa struct một nơi, và triển khai logic (`impl`) ở nơi khác. Macro (`println!`) làm vỡ luồng call graph thông thường.
- **Giải quyết**: 
  - Gộp các hàm bên trong `impl StructName` vào `children` của `ClassNode(StructName)`.
  - Xử lý `impl Trait for Struct` thành cấu trúc kế thừa và đưa vào `base_classes`.
  - Macros có thể được parse như một function call hoặc tạo riêng tag `@reference.macro` để lưu thành `CallNode` với flag `metadata: {"is_macro": true}`.

---

## Tổng kết quy trình chuyển đổi dự kiến (Parser Workflow)

Để triển khai được hệ thống này cho nhiều ngôn ngữ một cách mở rộng (scalable), quy trình nên theo thiết kế Adapter:

1. **Tree-sitter Parsing Phase**: Source code -> Concrete Syntax Tree (CST).
2. **Query Phase**: Chạy `tags.scm` (của hệ thống tự thiết kế, không dùng mặc định vì không đủ) trên CST.
3. **Language Adapter Phase**: Chuyển giao các captured nodes vào các adapter riêng (vd: `PythonAdapter(BaseAdapter)`). Các Adapter sẽ chịu trách nhiệm:
   - Instantiate các `UASTNode` subclass tương ứng.
   - Xử lý các Edge Cases, gộp nối (Go receiver, Rust Impl, TS arrow-functions).
   - Resolve các references đơn giản.
4. **Context Graph Builder**: Nhận UAST hoàn chỉnh và bắt đầu tạo các lệnh Cypher/SQL để insert Nodes/Edges vào Neo4j và embedding vào Vector Database.
