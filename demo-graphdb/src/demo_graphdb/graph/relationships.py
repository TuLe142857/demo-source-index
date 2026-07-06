from enum import Enum


class Rel(str, Enum):

    CONTAINS = "CONTAINS"

    DECLARES = "DECLARES"

    IMPORTS = "IMPORTS"

    CALLS = "CALLS"

    INHERITS = "INHERITS"

    DEFINES = "DEFINES"

    REFERENCES = "REFERENCES"