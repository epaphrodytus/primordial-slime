from oopsie.abstract_factory import Domain
from oopsie.abstract_factory import ConcreteGithubFactory, ConcreteBitbucketRepository

if __name__ == '__main__':
    domain = Domain()
    # The concrete repo factory is only referenced once, here:
    repo_factory = ConcreteGithubFactory()
    # The Repository object itself does not need to know what factory
    # it is receiving, it just needs to run the creation commands
    # that the AbstractRepositoryFactory Interface provides
    domain.init_repo(repo_factory)
    print("-----")
    print("Assume that we switch out the concrete repo_factory to another one")
    repo_factory = ConcreteBitbucketRepository()
    domain.init_repo(repo_factory)
    print("Thus concludes the abstract factory example")