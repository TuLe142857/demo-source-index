from enum import Enum


class Label(str, Enum):

    FILE = "File"

    CLASS = "Class"

    FUNCTION = "Function"

    METHOD = "Method"

    IMPORT = "Import"

    VARIABLE = "Variable"