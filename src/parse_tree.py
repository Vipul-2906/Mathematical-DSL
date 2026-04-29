class ParseTreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __repr__(self):
        return self._repr_tree("", True)

    def _repr_tree(self, prefix, is_last):
        result = prefix

        if prefix:
            result += "└── " if is_last else "├── "

        result += self.name + "\n"

        new_prefix = prefix + ("    " if is_last else "│   ")

        for i, child in enumerate(self.children):
            is_child_last = (i == len(self.children) - 1)
            result += child._repr_tree(new_prefix, is_child_last)

        return result