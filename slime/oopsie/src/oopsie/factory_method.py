from abc import ABC, abstractmethod

class AbstractBackend(ABC):
    def __init__(self):
        print(f"Initializing {self.__class__.__name__}")

    def link(self, frontend):
        print("[Backend] Linking self with given frontend")

class ConcretePrimaryBackend(AbstractBackend):
    """"""
    
class ConcreteSecondaryBackend(AbstractBackend):
    """"""

class AbstractFrontend(ABC):
    """"""
    def __init__(self):
        print(f"Initializing {self.__class__.__name__}")

class ConcretePrimaryFrontend(AbstractFrontend):
    """"""

class ConcreteSecondaryFrontend(AbstractFrontend):
    """"""

class Application:
    def __init__(self):
        print(f"Initializing {self.__class__.__name__}")

    def build(self):
        print(f"build() ran")
        backend = self.build_backend()
        frontend = self.build_frontend()
        backend.link(frontend)

    def build_backend(self):
        print("Constructing backend in build_backend() factory method")
        return ConcretePrimaryBackend()
    
    def build_frontend(self):
        print("Constructing frontend in build_frontend() factory method")
        return ConcretePrimaryFrontend()
    
class SubApplication(Application):
    def build_backend(self):
        print(f"Subclassed Application overrides build_backend() so that build() will use a different concrete backend instead")
        return ConcreteSecondaryBackend()

    def build_frontend(self):
        print(f"Subclassed Application override build_frontend() so that build() will use a different concrete frontend instead")
        return ConcreteSecondaryFrontend()
