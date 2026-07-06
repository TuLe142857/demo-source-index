from dataclasses import dataclass


@dataclass
class Function:

    id: str

    name: str

    start_line: int

    end_line: int

    file_path: str