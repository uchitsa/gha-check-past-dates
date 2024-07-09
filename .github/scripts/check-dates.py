import os
from github import Github
import re
from datetime import datetime

token = os.environ.get('GITHUB_TOKEN')
if token is None:
    raise ValueError('GITHUB_TOKEN env is not set')

gh = Github(token)
repo = gh.get_repo(os.environ.get('GITHUB_REPOSITORY'))
readme = repo.get_readme()
readme_content = readme.decoded_content.decode('utf-8')
