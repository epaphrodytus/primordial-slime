from oopsie.abstract_factory import Domain, Repository
from oopsie.abstract_factory import ConcreteGithubFactory

if __name__ == '__main__':
    domain = Domain()
    # The concrete repo factory is only referenced once, here:
    repo_factory = ConcreteGithubFactory()
    # The Repository object itself does not need to know what factory
    # it is receiving, it just needs to run the creation commands
    # that the AbstractRepositoryFactory Interface provides
    repo = Repository(repo_factory)
    domain.add(repo)
    domain.init(True)