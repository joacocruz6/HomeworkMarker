"""
TestCase class is a test input and output for running the tests and getting the answers
@author Joaquín Cruz
"""
class TestCase:
     def __init_(self,test_input:str,test_output:str):
          self.__test_input = test_input
          self.__test_output = test_output
     def getTestInput(self):
          return self.__test_input
     def getTestOutput(self):
          return self.__test_output
