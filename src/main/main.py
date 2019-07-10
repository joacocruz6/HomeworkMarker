import os
import sys
from pathlib import Path
src = Path('.').resolve().parent
sys.path.append(str(src))
from tester import PythonTester, AbstractTester,JavaTester,CTester,CPPTester,RubyTester
from optparse import OptionParser
from options import TestCase, TestOptions
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
def makeConfigurations(inputFile: str,outputFile: str) -> TestOptions:
     options = TestOptions()
     with open(inputFile,'r',encoding='utf-8') as f:
          for line in f:
               line = line[:-1]
               test = TestCase()
               test.setTestInput(line)
               options.add(test)
     with open(outputFile,'r',encoding='utf-8') as f:
          i = 0
          for line in f:
               line = line[:-1]
               options.getCase(i).setTestOutput(line)
               i+=1
     return options

if __name__=="__main__":
     #Creating the options of the console
     parser = OptionParser()
     parser.add_option("-t","--type",dest="filetype",action="store",type="string",help="Type of file to run, py to python, c for C, java for Java, etc...")
     parser.add_option("-f","--file",dest="filename",action="store",type="string",help="Name of the file to text without it's extension")
     parser.add_option("-i","--inputFile",dest="test_file",action="store",type="string",help="Route of the file where are the inputs")
     parser.add_option("-o","--outputFile",dest="output_file",action="store",type="string",help="Route of the file where are the outputs")
     parser.add_option("-d","--directory",dest="dir",action="store",type="string",help="Absolut path to the directory where we are going to work")
     (options,args)=parser.parse_args()
     fileType = options.filetype
     fileName = options.filename
     input_file = options.test_file
     output_file = options.output_file
     directory= options.dir
     test_config = makeConfigurations(input_file,output_file)
     
     testIn = list()
     testOut = list()
     for i in range(len(test_config)):
          case = test_config.getCase(i)
          testIn.append(case.getTestInput())
          testOut.append(case.getTestOutput())
     #Getting the file type and executing it's name
     if fileType == 'py':
          fileName = fileName+'.py'
          myTester = PythonTester(test_config,fileName)
     elif fileType == 'java':
          fileName = fileName+'.java'
          myTester = JavaTester(test_config,fileName)
     elif fileType == 'c':
          fileName = fileName + '.c'
          myTester = CTester(test_config,fileName)
     elif fileType == 'cpp':
          fileName = fileName + '.cpp'
          myTester = CPPTester(test_config,fileName)
     elif fileType == 'rb':
          fileName = fileName + '.rb'
          myTester = RubyTester(test_config,fileName)
     myTester.setCwd(directory)
     #We run the main from the tester defined
     main(myTester)