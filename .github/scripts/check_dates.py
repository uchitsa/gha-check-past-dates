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

date_pattern = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")


def date_in_past(date):
    return datetime.strptime(date, "%Y-%m-%d") < datetime.now()


new_readme_content = date_pattern.sub(lambda match: "closed" if date_in_past(match.group(0)) else match.group(0),
                                      readme_content)

if new_readme_content != readme_content:
    repo.update_file(readme.path, "update past dates to closed", new_readme_content, readme.sha)
