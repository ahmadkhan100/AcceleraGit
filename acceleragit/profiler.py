# acceleragit/profiler.py

import cProfile
import pstats
import io
import subprocess
import sys
import os

class Profiler:
    """
    Profiles the execution time of a Python script.
    """

    def __init__(self, entry_point):
        self.entry_point = entry_point

    def profile_code(self):
        profiler = cProfile.Profile()
        profiler.enable()
        try:
            subprocess.run([sys.executable, self.entry_point], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error during execution: {e}")
        profiler.disable()
        s = io.StringIO()
        ps = pstats.Stats(profiler, stream=s).sort_stats('tottime')
        ps.print_stats()
        return s.getvalue()
