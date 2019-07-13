import ast


def convert_ast_node(node: ast.AST) -> object:
    """Helper function to convert ast node object to python object
    :param node: ast node object
    :return: ast.Name or python object, one of: str, int, float, bool, tuple, list, dict
    """
    if isinstance(node, ast.Str):
        return node.s
    elif isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.NameConstant):  # boolean
        return node.value
    elif isinstance(node, ast.Tuple):
        return tuple(map(convert_ast_node, node.elts))
    elif isinstance(node, ast.List):
        return list(map(convert_ast_node, node.elts))
    elif isinstance(node, ast.Dict):
        return dict((convert_ast_node(k), convert_ast_node(v)) for k, v in zip(node.keys, node.values))
    elif isinstance(node, ast.Name):  # variable
        return node


def get_variable_value_from_source_code(source_code: str, variable_name: str) -> object:
    """
    Parse source code and find variable value by it's name.
    :param source_code: multi-line source code
    :param variable_name: str
    :return: variable value
    """
    found = False
    variable_value = None
    source_parsed = ast.parse(source_code)

    for node in source_parsed.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                # single variable assignment: "x = 1"
                if isinstance(target, ast.Name):
                    if target.id == variable_name:
                        variable_value = convert_ast_node(node.value)
                        found = True
                # multiple-assignment: "x, y = 0, 1"
                elif isinstance(target, (ast.Tuple, ast.List)) and isinstance(node.value, (ast.Tuple, ast.List)):
                    for element, value in zip(target.elts, node.value.elts):
                        if element.id == variable_name:
                            variable_value = convert_ast_node(value)
                            found = True

    if not found:
        raise NameError('Unresolved reference: variable "{}" is not found in source code!'.format(variable_name))

    return variable_value
