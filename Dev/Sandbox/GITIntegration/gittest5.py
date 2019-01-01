from pygit2 import clone_repository
repo_url = 'https://github.com/sasianu/Testo.git'
repo_path = 'C:\\Devworkspace\\GitWorkspace\\GITTEST'
repo = clone_repository(repo_url, repo_path) # Clones a non-bare repository
repo = clone_repository(repo_url, repo_path, bare=True) # Clones a bare rep