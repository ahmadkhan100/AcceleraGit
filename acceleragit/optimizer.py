# acceleragit/optimizer.py

import ast
import astunparse
from functools import lru_cache

class CodeOptimizer:
    """
    Optimizes Python code by transforming the AST.
    """

    def __init__(self, python_files):
        self.python_files = python_files

    def optimize_all_files(self):
        for file_path in self.python_files:
            self.optimize_file(file_path)

    def optimize_file(self, file_path):
        with open(file_path, 'r') as file:
            source_code = file.read()
        tree = ast.parse(source_code)
        optimizer = self.CodeTransformer()
        optimized_tree = optimizer.visit(tree)
        optimized_code = astunparse.unparse(optimized_tree)
        with open(file_path, 'w') as file:
            file.write(optimized_code)

    class CodeTransformer(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            if self.is_recursive_function(node):
                node = self.add_memoization(node)
            return self.generic_visit(node)

        def is_recursive_function(self, node):
            function_name = node.name
            for child in ast.walk(node):
                if isinstance(child, ast.Call) and getattr(child.func, 'id', None) == function_name:
                    return True
            return False

        def add_memoization(self, node):
            # Add 'from functools import lru_cache' if not already imported
            import_stmt = ast.ImportFrom(module='functools', names=[ast.alias(name='lru_cache', asname=None)], level=0)
            node.decorator_list.insert(0, ast.Name(id='lru_cache', ctx=ast.Load()))
            return node
