# Chuẩn hóa Tree-sitter Captures cho UAST Builder

Để xây dựng được UAST (Unified Abstract Syntax Tree) đồng nhất cho nhiều ngôn ngữ khác nhau, chúng ta cần quy định một bộ các **capture tags** (nhãn trích xuất) dùng chung. 
Bất kỳ ngôn ngữ nào (Python, Java, Go...) khi thiết lập file cấu hình truy vấn `queries/tags.scm` cũng phải tuân thủ việc ánh xạ cú pháp của ngôn ngữ đó về các tag trong danh sách chuẩn hóa này.

## 1. Cấu trúc chương trình (Definitions)
Các capture này dùng để định danh các Block/Scope quan trọng trong mã nguồn, tương ứng với các Subclass của `UASTNode`.

| Capture Tag | Ánh xạ sang UAST | Ý nghĩa | Ví dụ |
|---|---|---|---|
| `@definition.class` | `ClassNode` | Định nghĩa class, interface, struct, trait, enum. | `class User:` hoặc `public interface IUser` |
| `@definition.function` | `FunctionNode` | Định nghĩa hàm, phương thức (method). | `def save():` hoặc `public void init()` |
| `@definition.variable` | `VariableNode` | Khai báo biến, hằng số, thuộc tính (field). | `x = 10` hoặc `private int count;` |
| `@definition.import` | `ImportNode` | Câu lệnh import thư viện/module. | `import os` hoặc `using System;` |
| `@definition.parameter`| Tham số hàm | Định nghĩa tham số đầu vào của một hàm. | `(x: int, y: int)` |
| `@name` | Thuộc tính `name` | Tên định danh của Class, Function, hoặc Variable. Luôn đi kèm với các `@definition.*` ở trên để lấy ra tên chính xác. | Chữ `User` trong `class User` |

---

## 2. Truy xuất & Tương tác (References)
Dùng để hỗ trợ xây dựng Call Graph và Dependency Graph cơ bản ở mức Syntax (rất quan trọng trước khi tích hợp LSP).

| Capture Tag | Ý nghĩa | Ví dụ |
|---|---|---|
| `@reference.call` | Lời gọi hàm (Function invocation). Dùng để trích xuất mảng `calls` trong `FunctionNode`. | `user.save()` |
| `@reference.class` | Sử dụng class (Instantiating, Type hinting, Type casting). | `u: User` hoặc `new User()` |
| `@reference.import` | Tên của module/package đang được import, làm đích đến. | Chữ `os` trong `import os` |

---

## 3. Ngữ cảnh & Metadata (Context & Modifiers)
Cực kỳ quan trọng để lưu vào Vector Database, cung cấp context tối đa cho AI Agent.

| Capture Tag | Ánh xạ sang UAST | Ý nghĩa |
|---|---|---|
| `@comment` | Cập nhật `docstring` | Các dòng comment thông thường (`//`, `#`). Sẽ được gán cho Node liền kề bên dưới nó. |
| `@doc` | Cập nhật `docstring` | Docstring chính thức (ví dụ: `"""doc"""` trong Python, `/** doc */` trong Java/JS). |
| `@decorator` | Thuộc tính `metadata` | Decorator hoặc Annotations quyết định hành vi. Rất cần cho framework (VD: `@app.route()`, `@Override`). |
| `@modifier` | Mảng `modifiers` | Các từ khóa thay đổi tính chất của node (VD: `public`, `private`, `static`, `async`, `export`). |

---

## Hướng dẫn viết File Query (`tags.scm`) cho một ngôn ngữ mới

Mỗi ngôn ngữ sẽ có một file `.scm` riêng để map cấu trúc cú pháp đặc thù của nó sang các tag chuẩn trên.
**Quy tắc bắt buộc:** Luôn luôn phải capture nguyên cái node chứa toàn bộ source code của block đó thành `@definition.*`, và capture riêng node chứa tên định danh thành `@name`.

### Ví dụ file `queries/python/tags.scm`:
```scheme
;; Bắt định nghĩa Class
(class_definition
  name: (identifier) @name
  body: (block)?
) @definition.class

;; Bắt định nghĩa Hàm
(function_definition
  name: (identifier) @name
  parameters: (parameters) @definition.parameter
) @definition.function

;; Bắt Hàm có chứa Decorator
(decorated_definition
  (decorator) @decorator
  definition: (function_definition
    name: (identifier) @name
  ) @definition.function
)
```

### Ví dụ file `queries/java/tags.scm`:
```scheme
;; Bắt định nghĩa Method
(method_declaration
  modifiers: (modifiers)? @modifier
  type: _
  name: (identifier) @name
  parameters: (formal_parameters) @definition.parameter
) @definition.function
```

**Kết luận:** Nhờ bộ quy chuẩn này, dù AST của Tree-sitter trả về Node gốc có tên là `method_declaration` (Java) hay `function_definition` (Python), thì **UAST Builder** ở backend Python của chúng ta chỉ cần parse dựa trên tag `@definition.function` và `@name` để xử lý toàn bộ logic mà không cần phải viết IF/ELSE phân loại theo từng ngôn ngữ.