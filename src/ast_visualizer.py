from graphviz import Digraph



KEYWORDS = {"solve", "where", "find"}
OPERATORS = {"="}


def node_style(name):
    # decide color based on type
    if name in KEYWORDS:
        return {"style": "filled", "fillcolor": "lightblue"}
    elif name in OPERATORS:
        return {"style": "filled", "fillcolor": "lightcoral"}
    elif name.isdigit():
        return {"style": "filled", "fillcolor": "lightyellow"}
    elif name in {"SolveStmt", "Assignments", "Assignment"}:
        return {"style": "filled", "fillcolor": "lightgray"}
    else:
        return {"style": "filled", "fillcolor": "lightgreen"}


def visualize_parse_tree(parse_tree):
    dot = Digraph(comment="Parse Tree")
    dot.attr(rankdir="TB")  # Top to Bottom (clean hierarchy)

    counter = [0]

    def add_nodes(node, parent_id=None):
        node_id = str(counter[0])
        counter[0] += 1

        style = node_style(node.name)

        dot.node(node_id, node.name, **style)

        if parent_id is not None:
            dot.edge(parent_id, node_id)

        for child in node.children:
            add_nodes(child, node_id)

    add_nodes(parse_tree)

    dot.render("static/parse_tree_graph", format="png", cleanup=True)



def visualize_ast(ast):
    dot = Digraph(comment="AST")
    dot.attr(rankdir="TB")  # top-to-bottom layout

    # Root node
    dot.node("root", "Solve", style="filled", fillcolor="lightgray")

    # Formula node
    dot.node(
        "formula",
        f"Formula: {ast.formula}",
        style="filled",
        fillcolor="lightblue"
    )
    dot.edge("root", "formula")

    # Target node
    dot.node(
        "target",
        f"Target: {ast.target}",
        style="filled",
        fillcolor="lightgreen"
    )
    dot.edge("root", "target")

    # Assignments parent
    dot.node(
        "assignments",
        "Assignments",
        style="filled",
        fillcolor="lightyellow"
    )
    dot.edge("root", "assignments")

    # Individual assignments
    for i, assign in enumerate(ast.assignments):
        node_name = f"assign_{i}"

        dot.node(
            node_name,
            f"{assign.variable} = {assign.value}",
            style="filled",
            fillcolor="lightcoral"
        )

        dot.edge("assignments", node_name)

    # Save image
    dot.render("static/ast_graph", format="png", cleanup=True)

