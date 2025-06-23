import ast

class FunctionInfo:
    def __init__(self, name, lineno, length, has_docstring):
        self.name = name
        self.lineno = lineno
        self.length = length
        self.has_docstring = has_docstring

def analyze_file(filepath):
    with open(filepath, "r") as f:
        code = f.read()

    tree = ast.parse(code)
    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            name = node.name
            lineno = node.lineno
            has_docstring = bool(ast.get_docstring(node))
            length = (
                node.body[-1].lineno - node.body[0].lineno + 1
                if node.body else 0
            )
            functions.append(FunctionInfo(name, lineno, length, has_docstring))

    return functions
