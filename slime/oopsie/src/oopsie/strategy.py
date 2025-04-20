"""
As opposed to the Template Method
the Strategy pattern allows different algorithms
to be used via delegation.
The interface design is very important for this one.
"""

from abc import ABC, abstractmethod

class Metadata:
    def __init__(self, saver:"SaverInterface"):
        """"""
        print(f"Initializing {self.__class__.__name__} instance")
        self._saver = saver()
    
    def save(self):
        self._saver.save(self)

    def set_saver(self, saver):
        self._saver = saver()


class SaverInterface(ABC):
    def __init__(self):
        print(f"Initializing {self.__class__.__name__}")

    @abstractmethod
    def save(self, metadata:Metadata):
        """"""

class DatabaseSaver(SaverInterface):
    def save(self, metadata):
        print(f"Saving object {metadata.__class__.__name__} to database")

class FileBasedSaver(SaverInterface):
    def save(self, metadata):
        print(f"Saving object {metadata.__class__.__name__} to file")