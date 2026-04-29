class SolveNode:
    def __init__(self, formula, assignments, target):
        self.formula = formula
        self.assignments = assignments
        self.target = target

    def __repr__(self):
        result = "SolveNode\n"
        result += f"├── Formula: {self.formula}\n"
        result += f"├── Target: {self.target}\n"
        result += "└── Assignments\n"

        for i, assign in enumerate(self.assignments):
            if i == len(self.assignments) - 1:
                result += f"    └── {assign}\n"
            else:
                result += f"    ├── {assign}\n"

        return result


class AssignmentNode:
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

    def __repr__(self):
        return f"{self.variable} = {self.value}"