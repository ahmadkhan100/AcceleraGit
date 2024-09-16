# acceleragit/cli.py

import argparse
from acceleragit.repo_manager import RepoManager
from acceleragit.optimizer import CodeOptimizer
from acceleragit.profiler import Profiler
from acceleragit.report import PerformanceReport
from rich import print

def main():
    parser = argparse.ArgumentParser(description='AcceleraGit - Accelerate GitHub applications.')
    parser.add_argument('--repo', help='GitHub repository URL')
    parser.add_argument('--local-repo', help='Path to local repository')
    parser.add_argument('--entry-point', required=True, help='Entry point script of the application')
    args = parser.parse_args()

    if args.repo:
        repo_manager = RepoManager(repo_url=args.repo)
        print(f"[bold green]Cloning repository:[/bold green] {args.repo}")
        repo_manager.clone_repository()
    elif args.local_repo:
        repo_manager = RepoManager(local_path=args.local_repo)
        print(f"[bold green]Using local repository:[/bold green] {args.local_repo}")
    else:
        print("[bold red]Error:[/bold red] Please provide either a GitHub repository URL or a local repository path.")
        return

    entry_point = repo_manager.get_entry_point(args.entry_point)
    profiler = Profiler(entry_point)
    print("[bold cyan]Profiling before optimization...[/bold cyan]")
    before_stats = profiler.profile_code()

    optimizer = CodeOptimizer(repo_manager.get_python_files())
    print("[bold cyan]Optimizing code...[/bold cyan]")
    optimizer.optimize_all_files()

    print("[bold cyan]Profiling after optimization...[/bold cyan]")
    after_stats = profiler.profile_code()

    report = PerformanceReport(before_stats, after_stats)
    report.generate_report()

if __name__ == '__main__':
    main()
