import os
import sys
from pathlib import Path
src = Path('.').resolve().parent
sys.path.append(str(src))
from tester import PythonTester, AbstractTester,JavaTester,CTester,CPPTester,RubyTester
from optparse import OptionParser
testIn = ["0","4","2","10"]
testOut = ["1","5","2","33"]
"""
main: AbstractTester -> None
Given a tester, it compile it, run it process and the mark the test results of it
for the correction of homework.
"""
def main(tester: AbstractTester):
     tester.compileFile()
     tester.run()
     tester.mark()

if __name__=="__main__":
     #Creating the options of the console
     parser = OptionParser()
     parser.add_option("-t","--type",dest="filetype",action="store",type="string",help="Type of file to run, py to python, c for C, java for Java, etc...")
     parser.add_option("-f","--file",dest="filename",action="store",type="string",help="Name of the file to text without it's extension")
     (options,args)=parser.parse_args()
     fileType = options.filetype
     fileName = options.filename

     #Getting the file type and executing it's name
     if fileType == 'py':
          fileName = fileName+'.py'
          myTester = PythonTester(testIn,testOut,fileName)
     elif fileType == 'java':
          fileName = fileName+'.java'
          myTester = JavaTester(testIn,testOut,fileName)
     elif fileType == 'c':
          fileName = fileName + '.c'
          myTester = CTester(testIn,testOut,fileName)
     elif fileType == 'cpp':
          fileName = fileName + '.cpp'
          myTester = CPPTester(testIn,testOut,fileName)
     elif fileType == 'rb':
          fileName = fileName + '.rb'
          myTester = RubyTester(testIn,testOut,fileName)
     #We run the main from the tester defined
     main(myTester)