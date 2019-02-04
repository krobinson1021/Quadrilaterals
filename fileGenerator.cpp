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
        string filename = "/Users/katierobinson/Quadrilaterals/validQuadTesting/" + to_string(i) + ".txt";
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
    
    return 0;
}
