from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from business.guithub import GuitHub
from schema.guithub import GuitHubList, GuitHubFilter, GuitHubFilterList, GuitSearch
from config.guithub import github_client
from fastapi import Depends

github_router = InferringRouter()


@cbv(github_router)
class GuitHubRouter:

    @github_router.get("/all/")
    async def get_all(self) -> GuitHubList:
        return await GuitHub(github_client).get_all()

    @github_router.get("/search/name/")
    async def get_name_filter(self, name: str) -> GuitSearch:
        return await GuitHub(github_client).get_name_filter(name)

    @github_router.get("/search/filters/")
    async def get_filters(self, filter_schema: GuitHubFilter = Depends()) -> GuitHubFilterList:
        return await GuitHub(github_client).get_filter(filter_schema)
