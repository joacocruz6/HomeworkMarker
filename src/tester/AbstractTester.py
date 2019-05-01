import os
import sys
from abc import ABC
from pathlib import Path
my_path = Path('.').resolve().parent.parent #The project directory
src_path = Path('.').resolve().parent #The src directory
sys.path.append(my_path)
sys.path.append(src_path)

class AbstractTester(ABC):
     def __init__(self,test_file: str,tarea: str):
          self._test_file = test_file
          self._tarea = tarea
     def getTestFile(self):
          return self._test_file
     def getTarea(self):
          return self.tarea
     @abstractmethod
     def runFile(self):
          pass
     @abstractmethod
     def run(self):
          pass