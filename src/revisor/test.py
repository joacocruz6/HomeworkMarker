import os
import sys
from pathlib import Path
my_path = Path('.').resolve().parent.parent #The project directory
src_path = Path('.').resolve().parent #The src directory
sys.path.append(my_path)
sys.path.append(src_path)

class Main:
     def __init__(self):
          self.hello= "Hello"
     def showList(self):
          os.system('ls')
     def execute(self,program: str):
          instruction = "python3 "+program
          os.system(instruction)

def main(args: list):
     my_main = Main()
     my_main.showList()
     my_main.execute("test2.py")

if __name__=="__main__":
     main([])
