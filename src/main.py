import sys
from file_reader import read_source_file
from lexer import Lexer
from parser import Parser
# import parser
from solver import Solver
from file_writer import write_to_file
from ast_visualizer import visualize_ast, visualize_parse_tree

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <source_file.dsl>")
        return

    source_file = sys.argv[1]

    if not source_file.endswith(".mdsl"):
        print("Error: Only .mdsl files are supported")
        return

    content = read_source_file(source_file)

    if content is None:
        return

    lexer = Lexer(content)
    tokens = lexer.tokenize()

    token_output = ""
    for token in tokens:
        token_output += str(token) + "\n"

    write_to_file("tokens.txt", token_output)

    parser = Parser(tokens)
    parse_tree, ast = parser.parse()
    visualize_parse_tree(parse_tree)
    visualize_ast(ast)
    write_to_file("parse_tree.txt", str(parse_tree))
    write_to_file("ast.txt", str(ast))
    trace_output = ""
    for line in parser.trace:
        trace_output += line + "\n"

    write_to_file("parse_trace.txt", trace_output)


    solver = Solver()
    result = solver.solve(ast)
    print(result)

    pipeline = ""

    pipeline += "===== DSL INPUT =====\n"
    pipeline += content + "\n\n"

    pipeline += "===== TOKENS =====\n"
    for token in tokens:
        pipeline += str(token) + "\n"

    pipeline += "\n===== PARSER TRACE =====\n"
    for line in parser.trace:
        pipeline += line + "\n"

    pipeline += "\n===== AST =====\n"
    pipeline += str(ast) + "\n"

    pipeline += "\n===== RESULT =====\n"
    pipeline += str(result) + "\n"

    write_to_file("pipeline.txt", pipeline)


if __name__ == "__main__":
    main()