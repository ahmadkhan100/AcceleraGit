# AcceleraGit

**Accelerate your GitHub applications effortlessly.**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Option 1: Install via pip](#option-1-install-via-pip)
  - [Option 2: Standalone Executable](#option-2-standalone-executable)
- [Usage](#usage)
  - [Optimizing a GitHub Repository](#optimizing-a-github-repository)
  - [Optimizing a Local Repository](#optimizing-a-local-repository)
- [Example](#example)
  - [Step 1: Prepare a Sample Application](#step-1-prepare-a-sample-application)
  - [Step 2: Run AcceleraGit](#step-2-run-acceleragit)
  - [Expected Output](#expected-output)
- [How It Works](#how-it-works)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

**AcceleraGit** is a command-line tool designed to optimize Python applications hosted on GitHub, aiming to enhance their performance significantly. By analyzing code for inefficiencies and applying optimizations, AcceleraGit helps developers improve execution speed and resource utilization.

## Features

- **Automatic Repository Cloning**: Clone any public GitHub repository directly from the command line.
- **Static Code Analysis**: Analyze Python code to detect inefficient patterns using Abstract Syntax Trees (AST).
- **Code Optimization**: Apply transformations to improve performance, such as adding memoization to recursive functions.
- **Profiling**: Measure execution time before and after optimization using `cProfile`.
- **Performance Reporting**: Generate detailed reports comparing performance metrics with visual enhancements.
- **Easy Integration**: Simple command-line interface for quick optimization.
- **Extensibility**: Modular design allows for adding more optimization techniques.

## Installation

### Prerequisites

- **Python 3.7** or higher
- **Git** installed and accessible via the command line
- **pip** package manager

### Option 1: Install via `pip`

AcceleraGit is available on PyPI and can be installed using `pip`:

```bash
pip install acceleragit
```

Option 2: Standalone Executable
Download the standalone executable for your platform from the Releases page

For Windows:

```bash
acceleragit.exe --help
```
For macOS/Linux:

```bash
./acceleragit --help
```

Usage
AcceleraGit provides a simple command-line interface. You can optimize a GitHub repository or a local repository.

Optimizing a GitHub Repository

```bash
acceleragit --repo https://github.com/username/repo.git --entry-point main.py
```

--repo: URL of the GitHub repository to optimize.
--entry-point: The entry point script of the application.

Optimizing a Local Repository

```bash
acceleragit --local-repo ./path/to/repo --entry-point app.py
```
--local-repo: Path to the local repository.
--entry-point: The entry point script of the application.

Example
Let's optimize a sample application that calculates the Fibonacci sequence recursively.

Step 1: Prepare a Sample Application
Create a Python file app.py with the following content:

```main.py
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def main():
    print("Calculating Fibonacci(35)...")
    result = fibonacci(35)
    print(f"Result: {result}")

if __name__ == '__main__':
    main()
```
Step 2: Run AcceleraGit

```bash
acceleragit --local-repo ./ --entry-point app.py
```
Expected Output

```less

[bold green]Cloning repository:[/bold green] ./ 
[bold cyan]Profiling before optimization...[/bold cyan]
Calculating Fibonacci(35)...
Result: 9227465
[bold cyan]Optimizing code...[/bold cyan]
[bold cyan]Profiling after optimization...[/bold cyan]
Calculating Fibonacci(35)...
Result: 9227465

┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Metric                ┃ Before Optimization  ┃ After Optimization  ┃ Improvement   ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ Total Execution Time  │ 30.4567s             │ 0.0012s             │ 99.99%        │
└───────────────────────┴──────────────────────┴─────────────────────┴───────────────┘

```

How It Works
Repository Management: AcceleraGit clones the specified GitHub repository or accesses the local repository.
Profiling Before Optimization: Uses cProfile to profile the application before optimization.
Code Optimization:
Parses Python files into Abstract Syntax Trees (AST).
Transforms the AST to optimize code, e.g., adds memoization to recursive functions.
Writes the optimized code back to the files.
Profiling After Optimization: Profiles the optimized application.
Performance Reporting: Generates a report comparing execution times before and after optimization.
Limitations
Python Only: Currently supports only Python applications.
Optimization Scope: Limited to specific optimization techniques like memoization.
Entry Point Requirement: Requires knowledge of the application's entry point script.
Risk of Side Effects: Automatic code modifications may introduce bugs; always review optimized code.
Contributing
Contributions are welcome! Please follow these steps:

Fork the Repository: Click the "Fork" button at the top-right corner of this page.

Clone Your Fork:
```bash
git clone https://github.com/ahmadkhan100/AcceleraGit.git
```

Create a Branch:
```bash
git checkout -b feature/your-feature-name
```

Make Changes: Implement your feature or fix.

Run Tests:

```bash
python3 -m unittest discover tests
```
Commit Changes:
```bash
git commit -am 'Add new feature'
```

Push to Github:
```bash
git push origin feature/your-feature-name
```
Create a Pull Request: Go to the original repository and click "New Pull Request".

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Rich Library for beautiful console output.
GitPython for Git integration.
Open-source Community for providing inspiration and resources.


Disclaimer: AcceleraGit modifies code automatically. It is recommended to review changes and test thoroughly before deploying optimized applications.

Author: Ahmad Khan(ar5khan@uwaterloo.ca)



