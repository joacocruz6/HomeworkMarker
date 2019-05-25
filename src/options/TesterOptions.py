try:
     from TestCase import TestCase
except Exception as e:
     print(e)
class TestOptions:
     def __init__(self):
          self.__cases = list()
          self.__length = 0
     def __len__(self):
          return self.__length
     def add(self, case: TestCase):
          self.__cases.append(case)
          self.__length += 1
     def getCase(self,index: int):
          if index < 0 or index >= self.length:
               raise IndexError
          return self.__cases[index]