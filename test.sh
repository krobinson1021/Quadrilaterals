./main < squares.txt > output.txt
./main < rectangles.txt >> output.txt
./main < parallelograms.txt >> output.txt
./main < rhombi.txt >> output.txt
./main < kites.txt >> output.txt
./main < trapezoids.txt >> output.txt
./main < quadrilaterals.txt >> output.txt
diff output.txt expected_output.txt
