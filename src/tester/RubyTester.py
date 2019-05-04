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

class RubyTester(AbstractTester):
     def __init__(self,test_input: list, output: list,homework: str):
          super().__init__(test_input,output,homework)
     def compileFile(self):
          pass
     
     def run(self):
          for i in range(len(self.getInput())):
               p = subprocess.run(["ruby",self.getHomework()],input=self.getInput()[i],universal_newlines=True,stdout=subprocess.PIPE)
               self.getProcess().append(p)