from config.github import github_client
from schema.github import GitHubList, GitHubFilter, GitHubFilterList, GitHubSearch


class GitHub:

    def __init__(self, user):
        self.user = user.get_user()

    async def get_all(self) -> GitHubList:
        repositories = []
        for repo in self.user.get_repos():
            repositories.append(repo.name)
        total = len(repositories)
        return GitHubList(repositories=repositories, total=total)

    async def get_name_filter(self, name: str) -> GitHubSearch:
        path = f"{self.user.login}/{name}"
        repo = github_client.get_repo(path)
        return GitHubSearch(id=repo.id, name=repo.name, full_name=repo.full_name, language=repo.language)

    @staticmethod
    async def get_filter(filter_schema: GitHubFilter):
        repositories = []
        query_list = []

        if filter_schema.user:
            query_list.append(f"user:{filter_schema.user}")

        if filter_schema.readme:
            query_list.append(f"{filter_schema.readme} in:readme")

        if filter_schema.language:
            query_list.append(f"language:{filter_schema.language}")

        query = " ".join(str(x) for x in query_list)

        for i, repo in enumerate(
                github_client.search_repositories(
                    query=query,
                    sort=filter_schema.sort,
                    order=filter_schema.order,
                )
        ):
            repositories.append(repo.full_name)

            if i == filter_schema.limit - 1:
                break

        total = len(repositories)

        filters = GitHubFilter(
            user=filter_schema.user,
            language=filter_schema.language,
            readme=filter_schema.readme,
            sort=filter_schema.sort,
            order=filter_schema.order,
            limit=filter_schema.limit
        )
        return GitHubFilterList(repositories=repositories, total=total, filters=filters)

