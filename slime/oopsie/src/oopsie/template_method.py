from abc import ABC, abstractmethod

class ReleaseDocumentParser:
    def __init__(self):
        print(f"Initializing {self.__class__.__name__}")
        self._data = {}

    def read(self, path):
        print("Due to the various kinds of file that reading from is possible")
        print("Template method do_read_file() reads the file from wherever and converts it into a python dictionary")
        print("do_read_file() is also called a 'primitive operation'")
        print(f"With that said, reading from '{path}' with template method")
        data = self.do_read_file(path)
        self.validate(data)

    def validate(self, data:dict):
        print(f"Validating given python dictionary")
        return True

    def do_read_file(self, path):
        print("Default reading algorithm")
        return dict()


class ReleaseDocumentYmlParser(ReleaseDocumentParser):
    def do_read_file(self, path):
        print("Reading from YML File")
        return dict()
    
class ReleaseDocumentExcelParser(ReleaseDocumentParser):
    def do_read_file(self, path):
        print("Reading from Excel file")
        return dict()
