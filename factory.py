# when you don't know the type of object you want to create until runtime.
from abc import ABC, abstractmethod

class FileReader(ABC):
    @abstractmethod
    def read(self):
        print("reading file")
    
class txtFileReader(FileReader):
    def read(self):
        print("reading txt file")

class StrFileReader(FileReader):
    def read(self):
        print("reading str file")


class FileReaderFactory:
    @staticmethod
    def getReader(file_type):
        if(file_type == "txt"):
            return txtFileReader()
        elif(file_type == "str"):
            return StrFileReader()
        else:
            raise ValueError("Invalid file type")


userInput = "txt"
fileReader = FileReaderFactory.getReader(userInput)
fileReader.read()