# tests/test_optimizer.py

import unittest
import ast
import astunparse
from acceleragit.optimizer import CodeOptimizer

class TestCodeOptimizer(unittest.TestCase):

    def test_is_recursive_function(self):
        source_code = '''
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
'''
        tree = ast.parse(source_code)
        function_node = tree.body[0]
        optimizer = CodeOptimizer([])
        transformer = optimizer.CodeTransformer()
        self.assertTrue(transformer.is_recursive_function(function_node))

    def test_add_memoization(self):
        source_code = '''
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
'''
        expected_code = '''
@lru_cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
'''
        tree = ast.parse(source_code)
        function_node = tree.body[0]
        optimizer = CodeOptimizer([])
        transformer = optimizer.CodeTransformer()
        optimized_node = transformer.add_memoization(function_node)
        optimized_tree = ast.Module(body=[optimized_node], type_ignores=[])
        optimized_code = astunparse.unparse(optimized_tree).strip()
        self.assertIn('@lru_cache', optimized_code)

if __name__ == '__main__':
    unittest.main()
