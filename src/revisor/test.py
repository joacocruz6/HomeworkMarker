import os
import sys
import subprocess
from subprocess import Popen
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
     def changeDirectory(self):
          os.system('cd ..')
     def execute(self,program: str):
          instruction = "python3 "+program
          os.system(instruction)
     def execute_another_process(self,instruction:list,my_input:str):
          my_process = subprocess.run([x for x in instruction],input=my_input,universal_newlines=True,stdout=subprocess.PIPE)
          print(my_process)
          return my_process
def main(args: list):
     my_main = Main()
     other_process=my_main.execute_another_process(["python3","test2.py"],"Hola")
     print(other_process.stdout)
     #my_main.changeDirectory()
     #my_main.showList()
     #my_main.execute("test2.py")

if __name__=="__main__":
     main([])
