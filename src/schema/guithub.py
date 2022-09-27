from typing import Optional

from fastapi_utils.api_model import APIModel


class GuitHubList(APIModel):
    repositories: list = []
    total: int


class GuitHubFilter(APIModel):
    user: Optional[str]
    language: Optional[str]
    readme: Optional[str]
    sort: Optional[str] = "updated"
    order: Optional[str] = "asc"
    limit: int = 10


class GuitHubFilterList(GuitHubList):
    filters: GuitHubFilter


class GuitSearch(APIModel):
    id: int
    name: str
    full_name: str
    language: str
