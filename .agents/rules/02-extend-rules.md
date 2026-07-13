---
trigger: always_on
---

# Thư mục để đọc các rules:
- Root Repo: [rules](.)
    - Rule chính, tải sử dụng khi code các module trong repo
- Modules rules: <module>/.agents/rules/
    - Các module có thể có các setup rule mở rộng dành riêng cho module.

# Lưu ý:
- Luôn luôn tuân thủ rule ở root repo
- Khi code các chức năng của các module, load rule của các module đó và làm theo rule
- Độ ưu tiện:
    - Cao nhất: root repo rules
    - Tiếp đến: module rules(có thể có hoặc không)