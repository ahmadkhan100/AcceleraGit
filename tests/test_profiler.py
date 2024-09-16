# tests/test_profiler.py

import unittest
import os
from acceleragit.profiler import Profiler

class TestProfiler(unittest.TestCase):

    def setUp(self):
        self.script_path = './test_script.py'
        with open(self.script_path, 'w') as f:
            f.write('print("Hello World")')

    def tearDown(self):
        os.remove(self.script_path)

    def test_profile_code(self):
        profiler = Profiler(self.script_path)
        stats = profiler.profile_code()
        self.assertIn('function calls', stats)
        self.assertIn('Hello World', stats)  # Output from the script

if __name__ == '__main__':
    unittest.main()
