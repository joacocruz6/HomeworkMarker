import os
import sys
import subprocess
from pathlib import Path
"""
First we do some pathing options
"""
src_directory = Path('.').resolve().parent
project_directory = Path('.').resolve().parent.parent

sys.path.append(src_directory)
sys.path.append(project_directory)

"""
Some imports
"""
try:
     from .AbstractTester import AbstractTester
except ModuleNotFoundError:
     try:
          from AbstractTester import AbstractTester
     except ModuleNotFoundError as e:
          print(e)
"""
PythonTesterClass
This class creates a python tester to do test on python files
"""
class PythonTester(AbstractTester):
     def __init__(self,test_input: list, output: list,homework: str):
          super().__init__(test_input,output,homework)
     def compileFile(self):
          pass
     """
     run: None -> None
     Just run the functions and compare it's results as the
     runner
     """
     def run(self):
          for i in range(len(self.getInput())):
               p = subprocess.run(["python3",self.getHomework()],input=self.getInput()[i],universal_newlines=True,stdout=subprocess.PIPE)
               self.getProcess().append(p)
     
