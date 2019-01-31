all: main test coverage

main: main.cpp
	clang++ -c main.cpp
	clang++ -o main main.o

test: main
	chmod +x test.sh
	./test.sh

coverage:
	clang++ -fprofile-instr-generate -fcoverage-mapping main.cpp -o main
	LLVM_PROFILE_FILE="squares.profraw" ./main < squares.txt
	LLVM_PROFILE_FILE="rectangles.profraw" ./main < rectangles.txt
	LLVM_PROFILE_FILE="parallelograms.profraw" ./main < parallelograms.txt
	LLVM_PROFILE_FILE="rhombi.profraw" ./main < rhombi.txt
	LLVM_PROFILE_FILE="kites.profraw" ./main < kites.txt
	LLVM_PROFILE_FILE="trapezoids.profraw" ./main < trapezoids.txt
	LLVM_PROFILE_FILE="quadrilaterals.profraw" ./main < quadrilaterals.txt
	-LLVM_PROFILE_FILE="error1A.profraw" ./main < error1A.txt
	-LLVM_PROFILE_FILE="error1B.profraw" ./main < error1B.txt
	-LLVM_PROFILE_FILE="error1C.profraw" ./main < error1C.txt
	-LLVM_PROFILE_FILE="error1D.profraw" ./main < error1D.txt
	-LLVM_PROFILE_FILE="error1E.profraw" ./main < error1E.txt
	-LLVM_PROFILE_FILE="error1F.profraw" ./main < error1F.txt
	-LLVM_PROFILE_FILE="error1G.profraw" ./main < error1G.txt
	-LLVM_PROFILE_FILE="error1H.profraw" ./main < error1H.txt
	-LLVM_PROFILE_FILE="error2A.profraw" ./main < error2A.txt
	-LLVM_PROFILE_FILE="error2B.profraw" ./main < error2B.txt
	-LLVM_PROFILE_FILE="error3A.profraw" ./main < error3A.txt
	-LLVM_PROFILE_FILE="error3B.profraw" ./main < error3B.txt
	-LLVM_PROFILE_FILE="error3C.profraw" ./main < error3C.txt
	-LLVM_PROFILE_FILE="error3D.profraw" ./main < error3D.txt
	-LLVM_PROFILE_FILE="error3E.profraw" ./main < error3E.txt
	-LLVM_PROFILE_FILE="error3F.profraw" ./main < error3F.txt
	-LLVM_PROFILE_FILE="error3G.profraw" ./main < error3G.txt
	-LLVM_PROFILE_FILE="error3H.profraw" ./main < error3H.txt
	-LLVM_PROFILE_FILE="error4A.profraw" ./main < error4A.txt
	-LLVM_PROFILE_FILE="error4B.profraw" ./main < error4B.txt
	-LLVM_PROFILE_FILE="error4C.profraw" ./main < error4C.txt
	llvm-profdata merge -sparse main.profraw squares.profraw rectangles.profraw parallelograms.profraw rhombi.profraw kites.profraw trapezoids.profraw quadrilaterals.profraw error1A.profraw error1B.profraw error1C.profraw error1D.profraw error1E.profraw error1F.profraw error1G.profraw error1H.profraw error2A.profraw error2B.profraw error3A.profraw error3B.profraw error3C.profraw error3D.profraw error3E.profraw error3F.profraw error3G.profraw error3H.profraw error4A.profraw error4B.profraw error4C.profraw -o main.profdata
	llvm-cov show ./main -instr-profile=main.profdata

