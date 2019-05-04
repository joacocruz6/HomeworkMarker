import os
import sys
from pathlib import Path
src = Path('.').resolve().parent
sys.path.append(str(src))
from tester import PythonTester, AbstractTester,JavaTester

def main(args:list,tester: AbstractTester):
     tester.compileFile()
     tester.run()
     tester.mark()

if __name__=="__main__":
     #arg1 = "test2.py"
     #myTester = PythonTester(["0","4","2"],["2","5","2"],arg1)
     arg1 = "Hola.java"
     myTester = JavaTester(["0","4","2","10"],["1","5","2","33"],arg1)
     main([arg1],myTester)