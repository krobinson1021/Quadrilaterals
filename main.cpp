#include <fstream>
#include <iostream>
#include <iomanip>
#include <math.h>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

const double tolerance = 0.00001;
/*
 Struct representing a coordinate pair
 */
struct coordinatePair {
    double x;
    double y;
};

bool coordinatesCoincide(coordinatePair first, coordinatePair second) {
    return ((first.x == second.x) && (first.y == second.y));
}

/*
 Struct representing a quadrilateral, with the corners labeled in counterclockwise fashion
 */
struct quadrilateral {
    coordinatePair corner1;
    coordinatePair corner2;
    coordinatePair corner3;
    coordinatePair corner4;
} ;

/*
 Returns a vector of quadrilaterals populated the data from the vector of strings;
 strings converted to doubles to allow coordinate arithmetic;
 Each string in the vector must contain all 8 coordinates for a quadrilateral
 separated by spaces
 */
vector<quadrilateral> createQuadrsFromData(const vector<vector<string>>& data) {
    vector<quadrilateral> allQuadrilaterals;
    for (int i = 0; i < data.size(); i++) { // for each line in file, add points to quadrilateral
        quadrilateral q;
        q.corner1.x = 0.0;
        q.corner1.y = 0.0;
        try {
            q.corner2.x = stod(data[i][0]);
            q.corner2.y = stod(data[i][1]);
            q.corner3.x = stod(data[i][2]);
            q.corner3.y = stod(data[i][3]);
            q.corner4.x = stod(data[i][4]);
            q.corner4.y = stod(data[i][5]);
        } catch (const invalid_argument& ia) {
            cout << "error 1" << endl;
            exit (EXIT_FAILURE);
        } catch (const out_of_range& oor) {
            cout << "error 1" << endl;
            exit (EXIT_FAILURE);
        }
        if ((q.corner1.x > 100) || (q.corner1.x < 0) || (q.corner1.y > 100) || (q.corner1.y < 0) || (q.corner2.y > 100) || (q.corner2.y < 0) || (q.corner2.y > 100) || (q.corner2.y < 0) || (q.corner3.y > 100) || (q.corner3.y < 0) || (q.corner3.y > 100) || (q.corner3.y < 0) ||
            (q.corner4.y > 100) || (q.corner4.y < 0) || (q.corner4.y > 100) || (q.corner4.y < 0)) {
            cout << "error 1" << endl; // at least one point is outside range
            exit (EXIT_FAILURE);
        }
        if (coordinatesCoincide(q.corner1, q.corner2) || coordinatesCoincide(q.corner1, q.corner3) || coordinatesCoincide(q.corner1, q.corner4) || coordinatesCoincide(q.corner2, q.corner3) || coordinatesCoincide(q.corner2, q.corner4) || coordinatesCoincide(q.corner3, q.corner4)) {
            cout << "error 2" << endl; // at least two points coincide
            exit (EXIT_FAILURE);
        }
        allQuadrilaterals.push_back(q); // add quadrilateral to vector
    }
    return allQuadrilaterals;
}

/*
 Returns distance between two points;
 referenced from: https://www.geeksforgeeks.org/program-calculate-distance-two-points/
 */
double distance(double x1, double y1, double x2, double y2) {
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2) * 1.0);
}

/*
 Returns slope of the line between two points
 */
double slope(double x1, double y1, double x2, double y2) {
    if (x2 - x1 < tolerance) {
        return 1000000;
    }
    return ((y2 - y1) / (x2 - x1));
}

/*
 Returns true if quadrilateral has four right angles
 */
bool allRightAngles(const quadrilateral& q) {
    double slopeL = slope(q.corner1.x, q.corner1.y, q.corner4.x, q.corner4.y);
    double slopeR = slope(q.corner2.x, q.corner2.y, q.corner3.x, q.corner3.y);
    double slopeT = slope(q.corner4.x, q.corner4.y, q.corner3.x, q.corner3.y);
    double slopeB = slope(q.corner1.x, q.corner1.y, q.corner2.x, q.corner2.y);
    double negRecipSlopeL = -1.0 / slopeL;
    double negRecipSlopeR = -1.0 / slopeR;
    bool sidesAreVertical = (slopeL == 1000000) && (slopeR == 1000000) && (abs(slopeT) < tolerance) && (abs(slopeB) < tolerance);
    return sidesAreVertical;
}

/*
 Returns true if top and bottom sides of quadrilateral are parallel
 */
bool topAndBottomParallel(const quadrilateral& q) {
    double slopeB = slope(q.corner1.x, q.corner1.y, q.corner4.x, q.corner4.y);
    double slopeT = slope(q.corner2.x, q.corner2.y, q.corner3.x, q.corner3.y);
    return abs(slopeB - slopeT) < tolerance;
}

/*
 Returns true if left and right sides of quadrilateral are parallel
 */
bool leftAndRightParallel(const quadrilateral& q) {
    double slopeR = slope(q.corner4.x, q.corner4.y, q.corner3.x, q.corner3.y);
    double slopeL = slope(q.corner1.x, q.corner1.y, q.corner2.x, q.corner2.y);
    return (abs(slopeL - slopeR) < tolerance);
}

bool sidesEqualLength(quadrilateral q) {
    double lengthB = distance(q.corner1.x, q.corner1.y, q.corner2.x, q.corner2.y);
    double lengthL = distance(q.corner1.x, q.corner1.y, q.corner4.x, q.corner4.y);
    return abs(lengthB - lengthL) < tolerance;
}

/*
 Returns true if quadrilateral is a square
 */
bool isSquare(const quadrilateral& q) {
    return allRightAngles(q) && sidesEqualLength(q);
}

/*
 Returns true if quadrilateral is a rhombus
 */
bool isRhombus(const quadrilateral& q) {
    return sidesEqualLength(q) && topAndBottomParallel(q) && leftAndRightParallel(q);
}

/*
 Returns true if quadrilateral is a rectangle
 */
bool isRectangle(const quadrilateral& q) {
    return allRightAngles(q);
}

/*
 Returns true if quadrilateral is a parallelogram
 */
bool isParallelogram(const quadrilateral& q) {
    return topAndBottomParallel(q) && leftAndRightParallel(q);
}

/*
 Returns true if quadrilateral is a trapezoid
 */
bool isTrapezoid(const quadrilateral& q) {
    return  (topAndBottomParallel(q) && !leftAndRightParallel(q)) || (!topAndBottomParallel(q) && leftAndRightParallel(q));
}

/*
 Returns true if quadrilateral is a kite
 */
bool isKite(const quadrilateral& q) {
    double lengthB = distance(q.corner1.x, q.corner1.y, q.corner2.x, q.corner2.y);
    double lengthT = distance(q.corner3.x, q.corner3.y, q.corner4.x, q.corner4.y);
    double lengthL = distance(q.corner4.x, q.corner4.y, q.corner1.x, q.corner1.y);
    double lengthR = distance(q.corner2.x, q.corner2.y, q.corner3.x, q.corner3.y);
    return (lengthL == lengthB) && (lengthR == lengthT);
}

/*
 Prints the most specific classification of the quadrilateral to the console
 on its own line; if quadrilateral is not a square, rhombus, rectangle, parallelogram,
 kite, or trapezoid, it will print quadrilateral
 */
void printQuadrType(const quadrilateral& q) {
    if (isSquare(q)) {
        cout << "square";
    } else if (isRhombus(q)) {
        cout << "rhombus";
    } else if (isRectangle(q)) {
        cout << "rectangle";
    } else if (isParallelogram(q)) {
        cout << "parallelogram";
    } else if (isKite(q)) {
        cout << "kite";
    } else if (isTrapezoid(q)) {
        cout << "trapezoid";
    } else {
        cout << "quadrilateral";
    }
    cout << endl;
}

/*
 Will loop through all quadrilaterals in the vector and print
 their classification to the console on individual lines
 */
void outputAllClassifications(const vector<quadrilateral>& data) {
    for (int i = 0; i < data.size(); i++) {
        printQuadrType(data[i]);
    }
    cout << endl;
}

int main(int argc, const char * argv[]) {
    
    cout.precision(4);
    vector<vector<string>> allInput;
    string line;
    string delimiter = " ";
    while (!cin.eof()) { // as long as there is data to read and the end of the file is not reached
        getline(cin, line);
        istringstream ss(line);
        istream_iterator<string> begin(ss), end;
        vector<string> numbersInLine(begin, end); //putting each number in the vector
        if (numbersInLine.size() != 6) { // if line does not have the right number of points, quit
            cout << "error 1" << endl;
            exit (EXIT_FAILURE);
        }
        allInput.push_back(numbersInLine);
    }
    vector<quadrilateral> allQuadrilaterals = createQuadrsFromData(allInput);
    outputAllClassifications(allQuadrilaterals);
    
    return 0;
}
