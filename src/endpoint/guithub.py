from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from business.guithub import GuitHub
from schema.guithub import GuitHubList

github_router = InferringRouter()


@cbv(github_router)
class GuitHubRouter:

    @github_router.get("/all/")
    async def get_all(self) -> GuitHubList:
        return await GuitHub().get_all()

