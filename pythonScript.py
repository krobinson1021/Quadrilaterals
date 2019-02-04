#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 16:47:29 2019

@author: katierobinson
"""

import os
import glob
import subprocess
from subprocess import Popen, PIPE

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
    
for filepath in glob.iglob('/Users/katierobinson/Quadrilaterals/validQuadTesting/*.txt'):
    input = open(filepath, 'rb').read()
    running_proc = subprocess.Popen(['./main'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    out, err = running_proc.communicate(input=input)
    outfile = open("OUTPUT.txt", "w")
    outfile.write(out.decode())
    #subprocess.call(["diff", "allQuads_expectedOutput.txt", "OUTPUT.txt"])

#subprocess.call(["diff", "-w", "validQuadTesting/OUTPUT.txt", "allQuads_expectedOutput.txt"])

# run quadrilateral classifier on each test file
