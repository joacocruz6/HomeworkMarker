"""
Some useful imports
"""
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
This class creates a python tester to do test on python files.
:author: Joaquín Cruz
"""
class PythonTester(AbstractTester):
     """
     __init__: Constructor of the class, receive a list of test input, it's matching
     results of output and the name of the file to be tested. Creates an internal list
     of subprocess within it

     :self: Reference to the instance of the object
     :test_input: the input for the tests to be executed
     :test_output: list of correct outputs of the tests
     :homework: the name of the file to be executed
     :return: An instance of the class.
     """
     def __init__(self,test_input: list, output: list,homework: str):
          super().__init__(test_input,output,homework)
     """
     compileFile:
     Just pass because python does not compile
     """
     def compileFile(self):
          pass
     """
     run: 
     Just run the functions and save the process on the process list
     runner
     :self: The instance of the object
     """
     def run(self):
          for i in range(len(self.getInput())):
               p = subprocess.run(["python3",self.getHomework()],input=self.getInput()[i],universal_newlines=True,stdout=subprocess.PIPE)
               self.getProcess().append(p)
     
