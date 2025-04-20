from abc import ABC, abstractmethod

class AbstractRepositoryFactory(ABC):
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
    def create_team(self, repository):
        """"""
        print("Generating a Repo Team on Github")

    def create_repo(self, repository):
        """"""
        print("Generating a Repo on Github")

    def create_ruleset(self, repository):
        """"""
        print("Generating a Repo Ruleset on Github")

class ConcreteBitbucketRepository(AbstractRepositoryFactory):
    def create_team(self, repository):
        """"""
        print("Generating a Repo Team on Bitbucket")

    def create_repo(self, repository):
        """"""
        print("Generating a Repo on Bitbucket")

    def create_ruleset(self, repository):
        """"""
        print("Generating a Repo Ruleset on Bitbucket")



class BaseComponent(ABC):
    def __init__(self):
        self._child_map = dict()
        self._parent_map = dict()

    @property
    @abstractmethod
    def key(self):
        """"""

    @abstractmethod
    def init(self, recursive=False):
        if recursive:
            for component_key, component in self._child_map.items():
                component.init()

    def add(self, component:"BaseComponent"):
        if isinstance(component, BaseComponent):
            self._child_map[component.key] = component
            component._parent_map[self.key] = self
        else:
            raise TypeError
    

class Domain(BaseComponent):
    key = "domain"

    def init(self, recursive=False):
        print("Initializing Data Domain")
        super().init(recursive)

class Repository(BaseComponent):
    key = "repository"
    def __init__(self, platform:AbstractRepositoryFactory):
        self._platform = platform
        super().__init__()

    def init(self, recursive=False):
        self._platform.create_repo(self)
        super().init(recursive)

