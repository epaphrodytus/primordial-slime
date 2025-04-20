from abc import ABC, abstractmethod

class Repository(ABC):
    @property
    @abstractmethod
    def platform(self):
        """"""

class GithubRepository(Repository):
    @property
    def platform(self):
        return "GITHUB"

class BitbucketRepository(Repository):
    @property
    def platform(self):
        return "BITBUCKET"


class RepositoryTeam(ABC):
    @property
    @abstractmethod
    def platform(self):
        """"""
class GithubRepositoryTeam(RepositoryTeam):
    @property
    def platform(self):
        return "GITHUB"

class BitbucketRepositoryTeam(RepositoryTeam):
    @property
    def platform(self):
        return "BITBUCKET"


class RepositoryRuleset(ABC):
    @property
    @abstractmethod
    def platform(self):
        """"""

class GithubRepositoryRuleset(RepositoryRuleset):
    @property
    def platform(self):
        return "GITHUB"

class BitbucketRepositoryRuleset(RepositoryRuleset):
    @property
    def platform(self):
        return "BITBUCKET"


class AbstractRepositoryFactory(ABC):
    """
    Anybody who wants to run creation commands against a Repository
    can do so via this interface

    """
    @abstractmethod
    def create_team(self):
        """"""

    @abstractmethod
    def create_repo(self):
        """"""

    @abstractmethod
    def create_ruleset(self):
        """"""

class ConcreteGithubFactory(AbstractRepositoryFactory):
    def create_team(self):
        """"""
        print("Generating a Repo Team on Github")
        return GithubRepositoryTeam()

    def create_repo(self):
        """"""
        print("Generating a Repo on Github")
        return GithubRepository()

    def create_ruleset(self):
        """"""
        print("Generating a Repo Ruleset on Github")
        return GithubRepositoryRuleset()

class ConcreteBitbucketRepository(AbstractRepositoryFactory):
    def create_team(self):
        """"""
        print("Generating a Repo Team on Bitbucket")
        return BitbucketRepositoryTeam()

    def create_repo(self):
        """"""
        print("Generating a Repo on Bitbucket")
        return BitbucketRepository()

    def create_ruleset(self):
        """"""
        print("Generating a Repo Ruleset on Bitbucket")
        return BitbucketRepositoryRuleset()


class Domain:
    key = "domain"

    def init(self, recursive=False):
        print("Initializing Data Domain")
    
    def init_repo(self, repo_factory:AbstractRepositoryFactory):
        print("Domain is receiving a factory implementing the AbstractRepositoryFactory Interface")
        print("It does not know which exact factory it is using, it does not need to")
        repo = repo_factory.create_repo()
        repo_team = repo_factory.create_team()
        repo_ruleset = repo_factory.create_ruleset()
        return repo, repo_team, repo_ruleset

    

