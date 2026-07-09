from demo_ast.core import ParserFactory
from demo_ast.languages import get_language_configs, get_language_registry

language_configs = get_language_configs()
language_registry = get_language_registry()
parser_factory = ParserFactory(language_registry)
