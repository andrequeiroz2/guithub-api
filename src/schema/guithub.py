from fastapi_utils.api_model import APIModel


class GuitHubList(APIModel):
    repositories: list = []
    total: int