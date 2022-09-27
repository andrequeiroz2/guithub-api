from typing import Optional

from fastapi_utils.api_model import APIModel


class GitHubList(APIModel):
    repositories: list = []
    total: int


class GitHubFilter(APIModel):
    user: Optional[str]
    language: Optional[str]
    readme: Optional[str]
    sort: Optional[str] = "updated"
    order: Optional[str] = "asc"
    limit: int = 10


class GitHubFilterList(GitHubList):
    filters: GitHubFilter


class GitHubSearch(APIModel):
    id: int
    name: str
    full_name: str
    language: str
