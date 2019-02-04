#!/usr/bin/env python3

import os
import glob
import subprocess
from subprocess import Popen, PIPE
import filecmp
import time

# make organizational directories if they do not already exist
dirName = "validQuadTesting"
if not os.path.exists(dirName):
   os.mkdir(dirName)
    
dirName = "invalidError1Testing"
if not os.path.exists(dirName):
    os.mkdir(dirName)
    
dirName = "invalidError2Testing"
if not os.path.exists(dirName):
    os.mkdir(dirName)
    
dirName = "invalidError3Testing"
if not os.path.exists(dirName):
    os.mkdir(dirName)
    
dirName = "invalidError4Testing"
if not os.path.exists(dirName):
    os.mkdir(dirName)

dirName = "profFiles"
if not os.path.exists(dirName):
    os.mkdir(dirName)
    
# build C++ test file generator
subprocess.call(["clang++", "-c", "fileGenerator.cpp"])
subprocess.call(["clang++", "-o", "fileGenerator", "fileGenerator.o"]) 

# run generator to create random test files
subprocess.call("./fileGenerator")

# build C++ quadrilateral classifier
subprocess.call(["clang++", "-c", "main.cpp"])
subprocess.call(["clang++", "-o", "main", "main.o"])
    
# run classifier on each test file and print results
flag = True
for filepath in glob.iglob("validQuadTesting/*.txt"):
    input = open(filepath, "rb").read()
    running_proc = subprocess.Popen(["./main"], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    out, err = running_proc.communicate(input=input)
    outfile = open("OUTPUT.txt", "w")
    outfile.write(out.decode())
    outfile.flush()
    subprocess.Popen(["diff", "OUTPUT.txt", "allQuads_expectedOutput.txt"])
    if filecmp.cmp("OUTPUT.txt", "allQuads_expectedOutput.txt", shallow=True) == False:
        flag = False
if flag == True:
    print("OK")
else:
    print("ERROR")

# clean up by deleting old profraw and profdata files
profFileDirectory = "profFiles"
profFiles = os.listdir(profFileDirectory)
for file in profFiles:
    if file.endswith(".profraw") | file.endswith(".profdata"):
        os.remove(os.path.join(profFileDirectory, file))

# create fresh profraw files for each test case in preparation for coverage test
os.system("clang++ -fprofile-instr-generate -fcoverage-mapping main.cpp -o main")
i = 1
while i <= 1000:
    inputFilename = ''.join(["/Users/katierobinson/Quadrilaterals/validQuadTesting/", str(i), ".txt"])
    outputFilename = '"profFiles/' + str(i) + '.profraw"'
    llvmCommand = ''.join(["LLVM_PROFILE_FILE=", outputFilename])
    profrawGenCmd = ''.join([llvmCommand, " ./main < ", inputFilename, " > unnecessaryOutput.txt"])
    os.system(profrawGenCmd)
    i += 1
mergeCmd = "llvm-profdata merge -sparse "
i = 1
while i <= 1000:
    mergeCmd += "profFiles/" + str(i) + ".profraw "
    i += 1
mergeCmd += "-o " + "profFiles/main.profdata"
os.system(mergeCmd)