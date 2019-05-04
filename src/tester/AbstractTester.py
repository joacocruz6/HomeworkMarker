import os
import sys
from abc import *
from pathlib import Path
my_path = Path('.').resolve().parent.parent #The project directory
src_path = Path('.').resolve().parent #The src directory
sys.path.append(str(my_path))
sys.path.append(str(src_path))

class AbstractTester(ABC):
     def __init__(self,test_input: list,test_output: list,homework: str):
          self._test_input = test_input
          self._test_output = test_output
          self._homework = homework
          self._process = []
     def getHomework(self):
          return self._homework
     def getInput(self):
          return self._test_input
     def getOutput(self):
          return self._test_output
     def getProcess(self):
          return self._process
     @abstractmethod
     def compileFile(self):
          pass
     @abstractmethod
     def run(self):
          pass
     def mark(self):
          print("-------------------------------------")
          for i in range(len(self._process)):
               isCorrect = self._process[i].stdout[:-1] == self.getOutput()[i]
               if isCorrect:
                    print("Correct test number {}! Answer: {}".format(i+1,self._process[i].stdout[:-1]))
                    print("-------------------------------------")
               else:
                    print("Failed test number {}".format(i+1))
                    print("Expected value: {}".format(self.getOutput()[i]))
                    print("Homework returned: {}".format(self._process[i].stdout[:-1]))
                    print("-------------------------------------")