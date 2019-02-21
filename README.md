# Quadrilaterals

This repository contains Assignments 3-6 for CS 6015 Software Engineering. The program is a Quadrilateral Classifier that reads in counter-clockwise coordinates from an input file and returns shape classifications to an output file. I created a C++ program that generates thousands of random test files (some of which contain valid quadrilaterals and some that trigger different errors), as well as a Python script that automates the testing and diffs the classifier's output to the expected output.

Here are the possible classifications:

- square
- rhombus
- rectangle
- parallelogram
- kite
- trapezoid
- quadrilateral

# testFiles
This directory contains the expected output text files and the input file used for the automated test suite.

# coverage.txt
This file contains the llvm line coverage results. The Quadrilateral Classifier had 100% line coverage.

# pdfWriteups
This directory contains the test oracle and differential testing PDF writeups.

# archive
This directory contains the old Travis files from the continuous integration assignment, as well as the original manual testing .txt files.
