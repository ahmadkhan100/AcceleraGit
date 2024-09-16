# tests/test_report.py

import unittest
from acceleragit.report import PerformanceReport

class TestPerformanceReport(unittest.TestCase):

    def test_extract_total_time(self):
        before_stats = '''
         4 function calls in 0.005 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
         1    0.000    0.000    0.005    0.005 test_script.py:1(<module>)
         1    0.005    0.005    0.005    0.005 {built-in method builtins.print}
         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
'''
        after_stats = '''
         4 function calls in 0.003 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
         1    0.000    0.000    0.003    0.003 test_script.py:1(<module>)
         1    0.003    0.003    0.003    0.003 {built-in method builtins.print}
         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
'''
        report = PerformanceReport(before_stats, after_stats)
        before_time = report.extract_total_time(before_stats)
        after_time = report.extract_total_time(after_stats)
        self.assertEqual(before_time, 0.005)
        self.assertEqual(after_time, 0.003)

    def test_generate_report(self):
        before_stats = '''
         4 function calls in 0.005 seconds
'''
        after_stats = '''
         4 function calls in 0.003 seconds
'''
        report = PerformanceReport(before_stats, after_stats)
        # This will print the report; in a real test, you might redirect stdout
        report.generate_report()

if __name__ == '__main__':
    unittest.main()
