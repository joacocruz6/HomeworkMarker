try:
     from .TestCase import TestCase
except ModuleNotFoundError:
     try:
          from TestCase import TestCase
     except ModuleNotFoundError as e:
          print(e)
class TestOptions(object):
     def __init__(self):
          self.__cases = list()
          self.__length = 0
     def __len__(self):
          return self.__length
     def add(self, case: TestCase):
          self.__cases.append(case)
          self.__length += 1
     def __getitem__(self,key: int):
          if key < 0 or key >= self.__length:
               raise IndexError
          return self.__cases[key]

     """
     TODO: Deprecated
     
     """
     def getCase(self,index: int):
          if index < 0 or index >= self.__length:
               raise IndexError
          return self.__cases[index]