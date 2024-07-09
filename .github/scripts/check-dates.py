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

date_pattern = re.compile(
    r"^[0-9]{4}-(((0[13578]|(10|12))-(0[1-9]|[1-2][0-9]|3[0-1]))|(02-(0[1-9]|[1-2][0-9]))|((0[469]|11)-(0[1-9]|[1-2][0-9]|30)))$")
