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
    
# dirName = "invalidError4Testing"
# if not os.path.exists(dirName):
#     os.mkdir(dirName)

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
    
flag = True
# run classifier on each random valid test file
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

# run classifier on each random error1 test file
for filepath in glob.iglob("invalidError1Testing/*.txt"):
    input = open(filepath, "rb").read()
    running_proc = subprocess.Popen(["./main"], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    out, err = running_proc.communicate(input=input)
    outfile = open("OUTPUT.txt", "w")
    outfile.write(out.decode())
    outfile.flush()
    subprocess.Popen(["diff", "OUTPUT.txt", "error1_expectedOutput.txt"])
    if filecmp.cmp("OUTPUT.txt", "error1_expectedOutput.txt", shallow=True) == False:
        flag = False
        print(filepath)

# run classifier on each random error2 test file
for filepath in glob.iglob("invalidError2Testing/*.txt"):
    input = open(filepath, "rb").read()
    running_proc = subprocess.Popen(["./main"], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    out, err = running_proc.communicate(input=input)
    outfile = open("OUTPUT.txt", "w")
    outfile.write(out.decode())
    outfile.flush()
    subprocess.Popen(["diff", "OUTPUT.txt", "error2_expectedOutput.txt"])
    if filecmp.cmp("OUTPUT.txt", "error2_expectedOutput.txt", shallow=True) == False:
        flag = False
        print(filepath)

# run classifier on each random error3 test file
for filepath in glob.iglob("invalidError3Testing/*.txt"):
    input = open(filepath, "rb").read()
    running_proc = subprocess.Popen(["./main"], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    out, err = running_proc.communicate(input=input)
    outfile = open("OUTPUT.txt", "w")
    outfile.write(out.decode())
    outfile.flush()
    subprocess.Popen(["diff", "OUTPUT.txt", "error3_expectedOutput.txt"])
    if filecmp.cmp("OUTPUT.txt", "error3_expectedOutput.txt", shallow=True) == False:
        flag = False
        print(filepath)

# run classifier on each random error4 test file; NEVER TRIGGERED because all colinearity
# detected as line crossing
# for filepath in glob.iglob("invalidError4Testing/*.txt"):
#     input = open(filepath, "rb").read()
#     running_proc = subprocess.Popen(["./main"], stdout=PIPE, stdin=PIPE, stderr=PIPE)
#     out, err = running_proc.communicate(input=input)
#     outfile = open("OUTPUT.txt", "w")
#     outfile.write(out.decode())
#     outfile.flush()
#     subprocess.Popen(["diff", "OUTPUT.txt", "error4_expectedOutput.txt"])
#     if filecmp.cmp("OUTPUT.txt", "error4_expectedOutput.txt", shallow=True) == False:
#         flag = False
#         print(filepath)

# print results of all tests
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
while i <= 1000: # generating valid profraws
    inputFilename = ''.join(["/Users/katierobinson/Quadrilaterals/validQuadTesting/", str(i), ".txt"])
    outputFilename = '"profFiles/' + str(i) + '.profraw"'
    llvmCommand = ''.join(["LLVM_PROFILE_FILE=", outputFilename])
    profrawGenCmd = ''.join([llvmCommand, " ./main < ", inputFilename, " > unnecessaryOutput.txt"])
    os.system(profrawGenCmd)
    i += 1
while i <= 10: # generating error1 profraws
    inputFilename = ''.join(["/Users/katierobinson/Quadrilaterals/invalidError1Testing/", str(i), ".txt"])
    outputFilename = '"profFiles/e1_' + str(i) + '.profraw"'
    llvmCommand = ''.join(["LLVM_PROFILE_FILE=", outputFilename])
    profrawGenCmd = ''.join([llvmCommand, " ./main < ", inputFilename, " > unnecessaryOutput.txt"])
    os.system(profrawGenCmd)
    i += 1
while i <= 10: # generating error2 profraws
    inputFilename = ''.join(["/Users/katierobinson/Quadrilaterals/invalidError2Testing/", str(i), ".txt"])
    outputFilename = '"profFiles/e2_' + str(i) + '.profraw"'
    llvmCommand = ''.join(["LLVM_PROFILE_FILE=", outputFilename])
    profrawGenCmd = ''.join([llvmCommand, " ./main < ", inputFilename, " > unnecessaryOutput.txt"])
    os.system(profrawGenCmd)
    i += 1
while i <= 10: # generating error3 profraws
    inputFilename = ''.join(["/Users/katierobinson/Quadrilaterals/invalidError3Testing/", str(i), ".txt"])
    outputFilename = '"profFiles/e3_' + str(i) + '.profraw"'
    llvmCommand = ''.join(["LLVM_PROFILE_FILE=", outputFilename])
    profrawGenCmd = ''.join([llvmCommand, " ./main < ", inputFilename, " > unnecessaryOutput.txt"])
    os.system(profrawGenCmd)
    i += 1

# while i <= 10: # generating error4 profraws
#     inputFilename = ''.join(["/Users/katierobinson/Quadrilaterals/invalidError4Testing/", str(i), ".txt"])
#     outputFilename = '"profFiles/e4_' + str(i) + '.profraw"'
#     llvmCommand = ''.join(["LLVM_PROFILE_FILE=", outputFilename])
#     profrawGenCmd = ''.join([llvmCommand, " ./main < ", inputFilename, " > unnecessaryOutput.txt"])
#     os.system(profrawGenCmd)
#     i += 1

# merge all profraw files
mergeCmd = "llvm-profdata merge -sparse "
for filepath in glob.iglob("profFiles/*.profraw"):
    mergeCmd += filepath + " "
mergeCmd += "-o " + "profFiles/main.profdata"
os.system(mergeCmd)

