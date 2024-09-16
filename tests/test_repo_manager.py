# tests/test_repo_manager.py

import unittest
import os
from acceleragit.repo_manager import RepoManager

class TestRepoManager(unittest.TestCase):

    def setUp(self):
        self.local_repo = './test_repo'
        os.makedirs(self.local_repo, exist_ok=True)
        with open(os.path.join(self.local_repo, 'test.py'), 'w') as f:
            f.write('print("Hello World")')

    def tearDown(self):
        # Clean up the test repository
        import shutil
        shutil.rmtree(self.local_repo)

    def test_get_python_files(self):
        repo_manager = RepoManager(local_path=self.local_repo)
        python_files = repo_manager.get_python_files()
        self.assertEqual(len(python_files), 1)
        self.assertTrue(python_files[0].endswith('test.py'))

    def test_get_entry_point(self):
        repo_manager = RepoManager(local_path=self.local_repo)
        entry_point = repo_manager.get_entry_point('test.py')
        self.assertTrue(os.path.exists(entry_point))

        with self.assertRaises(FileNotFoundError):
            repo_manager.get_entry_point('nonexistent.py')

if __name__ == '__main__':
    unittest.main()
