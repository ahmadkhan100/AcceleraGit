# acceleragit/report.py

from rich.console import Console
from rich.table import Table
import re

class PerformanceReport:
    """
    Generates a performance report based on profiling data.
    """

    def __init__(self, before_stats, after_stats):
        self.before_stats = before_stats
        self.after_stats = after_stats

    def generate_report(self):
        console = Console()
        table = Table(title="Performance Comparison")

        table.add_column("Metric", style="cyan", no_wrap=True)
        table.add_column("Before Optimization", style="magenta")
        table.add_column("After Optimization", style="green")
        table.add_column("Improvement", style="yellow")

        before_time = self.extract_total_time(self.before_stats)
        after_time = self.extract_total_time(self.after_stats)
        if before_time > 0:
            improvement = ((before_time - after_time) / before_time) * 100
        else:
            improvement = 0.0

        table.add_row(
            "Total Execution Time",
            f"{before_time:.4f}s",
            f"{after_time:.4f}s",
            f"{improvement:.2f}%"
        )

        console.print(table)

    def extract_total_time(self, stats):
        # Extract total time from the profiling stats
        match = re.search(r'(\d+\.\d+) function calls.*in (\d+\.\d+) seconds', stats)
        if match:
            total_time = float(match.group(2))
            return total_time
        else:
            return 0.0
