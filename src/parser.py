from email.mime import message
from parse_tree import ParseTreeNode
from ast_nodes import SolveNode, AssignmentNode

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
        self.trace = []

    def log(self, message):
        self.trace.append(message)

    def current_token(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None

    def eat(self, expected_type=None, expected_value=None):
        token = self.current_token()

        if token is None:
            raise Exception("Parser Error: Unexpected end of input")

        if expected_type and token.type != expected_type:
            raise Exception(
                f"Parser Error: Expected {expected_type} but got {token.type} at line {token.line}"
            )

        if expected_value and token.value != expected_value:
            raise Exception(
                f"Parser Error: Expected '{expected_value}' but got '{token.value}' at line {token.line}"
            )

        self.position += 1
        return token

    def parse(self):
        self.log("Starting parsing process")
        
        parse_tree, ast = self.parse_solve_block()
        
        self.log("Parsing completed successfully")
        
        return parse_tree, ast


    def parse_solve_block(self):
        root = ParseTreeNode("SolveStmt")

        # solve
        self.eat("KEYWORD", "solve")
        root.add_child(ParseTreeNode("solve"))

        # formula
        formula_token = self.eat("IDENTIFIER")
        root.add_child(ParseTreeNode(formula_token.value))

        # where
        self.eat("KEYWORD", "where")
        root.add_child(ParseTreeNode("where"))

        assignments_node = ParseTreeNode("Assignments")
        assignments = []

        # first assignment
        pt_node, ast_node = self.parse_assignment()
        assignments_node.add_child(pt_node)
        assignments.append(ast_node)

        # more assignments
        while self.current_token() and self.current_token().type == "COMMA":
            self.eat("COMMA")
            pt_node, ast_node = self.parse_assignment()
            assignments_node.add_child(pt_node)
            assignments.append(ast_node)

        root.add_child(assignments_node)

        # find
        self.eat("KEYWORD", "find")
        root.add_child(ParseTreeNode("find"))

        # target
        target_token = self.eat("IDENTIFIER")
        root.add_child(ParseTreeNode(target_token.value))

        # AST creation
        ast = SolveNode(
            formula=formula_token.value,
            assignments=assignments,
            target=target_token.value
        )

        return root, ast

    def parse_assignment(self):
        var_token = self.eat("IDENTIFIER")
        self.eat("OPERATOR", "=")
        value_token = self.eat("NUMBER")

        # Parse Tree node
        pt_node = ParseTreeNode("Assignment")
        pt_node.add_child(ParseTreeNode(var_token.value))
        pt_node.add_child(ParseTreeNode("="))
        pt_node.add_child(ParseTreeNode(str(value_token.value)))

        # AST node
        ast_node = AssignmentNode(var_token.value, value_token.value)

        return pt_node, ast_node