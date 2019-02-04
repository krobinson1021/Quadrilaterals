#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import subprocess
from subprocess import Popen, PIPE
import filecmp

# make directories if they do not already exist
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
    
# build C++ test file generator
subprocess.call(["clang++", "-c", "fileGenerator.cpp"])
subprocess.call(["clang++", "-o", "fileGenerator", "fileGenerator.o"]) 

# create quadrilateral test files
subprocess.call("./fileGenerator")

# build C++ quadrilateral classifier
subprocess.call(["clang++", "-c", "main.cpp"])
subprocess.call(["clang++", "-o", "main", "main.o"])
    
# run quadrilateral classifier on each test file
for filepath in glob.iglob("validQuadTesting/*.txt"):
    input = open(filepath, "rb").read()
    running_proc = subprocess.Popen(["./main"], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    out, err = running_proc.communicate(input=input)
    outfile = open("OUTPUT.txt", "w")
    outfile.write(out.decode())
    subprocess.call(["diff", "-w", "-B", "OUTPUT.txt", "allQuads_expectedOutput.txt"])
    if os.stat("OUTPUT.txt").st_size == 0:
        subprocess.call(["open", filepath])