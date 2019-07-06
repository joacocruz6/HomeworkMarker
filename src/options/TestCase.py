"""
TestCase class is a test input and output for running the tests and getting the answers
@author Joaquín Cruz
"""
class TestCase:
     def __init_(self):
          self.__test_input = ""
          self.__test_output = ""
     def getTestInput(self):
          return self.__test_input
     def getTestOutput(self):
          return self.__test_output
     def setTestInput(self,my_input: str):
          self.__test_input = my_input
     def setTestOutput(self,expected: str):
          self.__test_output = expected
