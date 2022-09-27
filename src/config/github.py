from github import Github
from config.config import settings

github_client = Github(settings.GITHUB_TOKEN)
