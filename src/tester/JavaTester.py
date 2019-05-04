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

class JavaTester(AbstractTester):

     """
     The constructor of the class
     """
     def __init__(self,test_input: list, output: list,homework: str):
          super().__init__(test_input,output,homework)
          self.runClass = homework.split(".java")[0]
     """
     """
     def compileFile(self):
          subprocess.run(["javac",self.getHomework()])
     def run(self):
          for i in range(len(self.getInput())):
               p = subprocess.run(["java",self.runClass],input=self.getInput()[i],universal_newlines=True,stdout=subprocess.PIPE)
               self.getProcess().append(p)