# acceleragit/repo_manager.py

import os
from git import Repo

class RepoManager:
    """
    Manages cloning and handling of repositories.
    """

    def __init__(self, repo_url=None, local_path=None):
        self.repo_url = repo_url
        self.local_path = local_path or './cloned_repo'

    def clone_repository(self):
        if os.path.exists(self.local_path):
            print("Repository already exists locally.")
        else:
            Repo.clone_from(self.repo_url, self.local_path)

    def get_python_files(self):
        python_files = []
        for root, dirs, files in os.walk(self.local_path):
            for file in files:
                if file.endswith('.py'):
                    python_files.append(os.path.join(root, file))
        return python_files

    def get_entry_point(self, entry_point):
        entry_path = os.path.join(self.local_path, entry_point)
        if not os.path.exists(entry_path):
            raise FileNotFoundError(f"Entry point '{entry_point}' not found in the repository.")
        return entry_path
