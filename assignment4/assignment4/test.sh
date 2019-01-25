./main < squares.txt | grep 'square tests passed' &&
./main < rectangles.txt | grep 'rectangle tests passed' &&
./main < parallelograms.txt | grep 'parallelogram tests passed' &&
./main < rhombi.txt | grep 'rhombi tests passed' &&
./main < trapezoids.txt | grep 'trapezoid tests passed' &&
./main < kites.txt | grep 'kite tests passed' &&
./main < quadrilaterals.txt | grep 'quadrilateral tests passed'
