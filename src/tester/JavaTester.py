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
from options import TestCase, TestOptions
class JavaTester(AbstractTester):

     """
     The constructor of the class
     """
     def __init__(self,options:TestOptions,homework: str):
          super().__init__(options,homework)
          self.runClass = homework.split(".java")[0]
     """
     """
     def compileFile(self):
          subprocess.run(["javac",self.getHomework()],cwd=self._cwd)
     def run(self):
          for i in range(len(self.getOptions())):
               p = subprocess.run(["java",self.runClass],input=self.getOptions()[i].getTestInput(),universal_newlines=True,stdout=subprocess.PIPE,cwd=self._cwd)
               self.getProcess().append(p)