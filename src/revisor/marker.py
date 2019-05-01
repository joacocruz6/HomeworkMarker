import os
import sys
import subprocess
from subprocess import Popen
from pathlib import Path
my_path = Path('.').resolve().parent.parent #The project directory
src_path = Path('.').resolve().parent #The src directory
sys.path.append(my_path)
sys.path.append(src_path)

class Marker:
     def __init__(self,archivo: str,numeroTest: int):
          self.archivo = archivo
          self.numeroTest = numeroTest
     def runTest(self,inputs,output_esperados):
          procesos = []
          for i in range(self.numeroTest):
               p = subprocess.run(["python3",self.archivo],input=inputs[i],universal_newlines=True,stdout=subprocess.PIPE)
               procesos.append(p)
          for i in range(self.numeroTest):
               paso = procesos[i].stdout[:-1] == output_esperados[i]
               if paso:
                    print("Test numero {} pasado!".format(i))
               else:
                    print("Test numero {} no pasado".format(i))
                    print("Resultado esperado: {}".format(output_esperados[i]))
                    print("Resultado obtenido por el alumno: {}".format(procesos[i].stdout))

def main():
     m = Marker("test2.py",3)
     m.runTest(["0","4","2"],["1","5","2"])
if __name__=="__main__":
     main()
