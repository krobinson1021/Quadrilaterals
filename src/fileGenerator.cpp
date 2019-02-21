#include <fstream>
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string>
#include <vector>

using namespace std;

int main(int argc, const char * argv[]) {
    
    // generating 1000 random text files with valid quadrilateral data
    vector<vector<string> > allLines;
    string line;
    string delimiter = " ";
    ifstream infile;
    infile.open ("allQuads_input.txt");

    while(!infile.eof()) {
        getline(infile,line);
        istringstream ss(line);
        istream_iterator<string> begin(ss), end;
        vector<string> parsedLine(begin, end);
        if (line.length() != 0) {
            allLines.push_back(parsedLine);
        }
    }
    infile.close();

    for (int i = 1; i <= 1000; i++) {
        string filename = "validQuadTesting/" + to_string(i) + ".txt";
        ofstream textFile (filename);
        srand (time(NULL));
        int scalingFactor = rand() % 10 + 1; // nothing in the input text file has a coordinate bigger than 10
        for (int j = 0; j < allLines.size(); j++) {
            for (int k = 0; k < allLines[j].size(); k++) { // for each x or y value in the line
                textFile << (stoi(allLines[j][k]) * scalingFactor);
                if (k != 5) {
                    textFile << " ";
                }
            }
            if (j != allLines.size() - 1) {
                textFile << endl;
            }
        }
        textFile.close();
    }

    // generating 10 random text files with error1 data
    for (int i = 1; i <= 10; i++) {
        string filename = "invalidError1Testing/" + to_string(i) + ".txt";
        ofstream textFile (filename);
        int numToPrint = rand() % 20 + 1;
        for (int k = 0; k < numToPrint; k++) {    
            int r = rand() % 78;   // generate a random number
            char c = '0' + r;      // Convert to a char
            textFile << c;
            if (r % 2 == 0) {
                textFile << " ";
            }
            if (k == 4 || k == 7 || k == 9 || k == 11) {
                textFile << "\n";
            }
            if (k == 15) {
                textFile << "\n\n";
            }
        }
    }

    // generating 10 random text files with error2 data
    for (int i = 1; i <= 10; i++) {
        string filename = "invalidError2Testing/" + to_string(i) + ".txt";
        ofstream textFile (filename);
        for (int k = 0; k < 4; k++) {    
            int r = rand() % 101;   // generate a random number between 1 and 100
            textFile << r;
            if (k < 5) {
                textFile << " ";
            }
        }
        textFile << 0 << " " << 0; // guarantees a point will coincide
    }

    // generating 10 random text files with error3 data
    int crossingCoordinates1[6] = {3, 3, 4, 7, 8, 9};
    int crossingCoordinates2[6] = {1, 0, 1, 2, 2, 1};
    for (int i = 1; i <= 10; i++) {
        string filename = "invalidError3Testing/" + to_string(i) + ".txt";
        ofstream textFile (filename);
        int scalingFactor = rand() % 10 + 1;   // generate a random number between 1 and 10
        if (i < 5) {
            for (int k = 0; k < 6; k++) {
                textFile << (scalingFactor * crossingCoordinates1[k]);
                if (k != 5) {
                    textFile << " ";
                }
            }
        } else {
            for (int k = 0; k < 6; k++) {
                textFile << (scalingFactor * crossingCoordinates2[k]);
                if (k != 5) {
                    textFile << " ";
                }
            }
        }
    }

    // generating 10 random text files with error4 data
    int colinearY[6] = {9, 1, 2, 1, 2, 1};
    int colinearX[6] = {1, 4, 1, 3, 1, 8};
    for (int i = 1; i <= 10; i++) {
        string filename = "invalidError4Testing/" + to_string(i) + ".txt";
        ofstream textFile (filename);
        int scalingFactor = rand() % 10 + 1;   // generate a random number between 1 and 10
        if (i < 5) {
            for (int k = 0; k < 6; k++) {
                textFile << (scalingFactor * colinearY[k]);
                if (k != 5) {
                        textFile << " ";
                }
            }
        } else {
           for (int k = 0; k < 6; k++) {
                textFile << (scalingFactor * colinearX[k]);
                if (k != 5) {
                        textFile << " ";
                }
            } 
        }
    }

}

