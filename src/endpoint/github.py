from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from business.github import GitHub
from schema.github import GitHubList, GitHubFilter, GitHubFilterList, GitHubSearch, AlphabeticalFilter
from config.github import github_client
from fastapi import Depends

github_router = InferringRouter()


@cbv(github_router)
class GitHubRouter:

    @github_router.get("/all/")
    async def get_all(self, filter_schema: AlphabeticalFilter = Depends()) -> GitHubList:
        return await GitHub(github_client).get_all(filter_schema)

    @github_router.get("/search/name/")
    async def get_name_filter(self, name: str) -> GitHubSearch:
        return await GitHub(github_client).get_name_filter(name)

    @github_router.get("/search/filters/")
    async def get_filters(self, filter_schema: GitHubFilter = Depends()) -> GitHubFilterList:
        return await GitHub(github_client).get_filter(filter_schema)
