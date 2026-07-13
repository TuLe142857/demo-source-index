---
trigger: always_on
---

# Project Context:
- Đây là một mono repo dùng phục vụ bước demo/kiểm thử công nghệ cho một project khác:
    - Tìm hiểu tech-stack/thư viện
    - Kiểm tra tính khả thi của teck-stack/thư viện
    - Viết một vài module để chạy thử
    - Design các tính năng cần thiết(optional) dưới dạng các module lẻ cho project
- Project chính(project mà repo này phục vụ demo):
    - "Xây dụng hệ thống cung cấp context cho coding agent thông qua giao thức MCP"
    - Công nghệ sử dụng dự kiến:
        - Primary programming language: Python
        - Server: FastAPI(có thể thay đổi), dùng để chứa logic parse code, quản lý graph database, quản lý nghiệp vụ chính, cung cấp API....
        - Tree-sitter: parse code
        - MCP-SDK: build local mcp server(giao tiếp stdio) để agent gọi. Agent sẽ không gọi trức tiếp API mà thông qua MCP làm lớp trung gian(đồng thời đảm nhận luôn việc Auth bằng cách 
        cấu hình commandline mcp - truyền token chẳn hạn)
        - Vì vẫn trong quá trình phân tích nghiệp vụ, tìm hiểu tech stack nên các công nghệ trên có thể thay đổi trong quá trình phát triển

# This Repos structure and rules:
## Với các module demo code bằng python(chiếm đa số):
- Dùng build tool **uv**
- Setup virtual workspace:
    - File  [pyproject.toml](../../pyproject.toml) dùng cấu hình workspace cũng như setup các config default cho các member
    - Mỗi member workspace sẽ là một module độc lập, có dependencies riêng(trừ pytest/ruff đã được cài ở workspace với group='dev')
- Mỗi module phụ vụ tìm hiểu nghiên cứu một chức năng/techstack độc lập.
- Giai đoạn đầu, các module có thể tách biệt không phụ thuộc nhau
- Giai đoạn sau, nếu cần kiểm tra tính phối hợp tạo thành workflow của hệ thống, các module có thể gọi lẫn nhau(ví dụ module `demo-graph-db` có thể cần gọi `demo-ast-parser` để test flow parse-code -> lưu vào vector-db)
