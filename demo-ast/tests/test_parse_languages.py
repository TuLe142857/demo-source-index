from demo_ast.parser import ParserFactory


def test_parse_python(parser_factory: ParserFactory):
    source = b"""
def run():
    print("hello")
    """
    parser = parser_factory.get_parser("python")
    tree = parser.parse(source)
