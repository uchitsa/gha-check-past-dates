import os

token = os.environ.get('GITHUB_TOKEN')
if token is None:
    raise ValueError('GITHUB_TOKEN env is not set')
