from config.guithub import github_client
from schema.guithub import GuitHubList


class GuitHub:
    @staticmethod
    async def get_all() -> GuitHubList:
        repositories = []
        for repo in github_client.get_user().get_repos():
            repositories.append(repo.name)
            print(repo.name)
        total = len(repositories)
        return GuitHubList(repositories=repositories, total=total)

