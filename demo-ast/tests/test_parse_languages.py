from demo_ast.core import ParserFactory


def test_parse_python(parser_factory: ParserFactory):
    source = b"""
def run():
    print("hello")
    """
    parser = parser_factory.get_parser("python")
    parser.parse(source)
