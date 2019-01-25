all: main

main: main.cpp
	g++ -o main.o -c main.cpp

test: main
	chmod +x test.sh
	./test.sh

coverage:
	clang++ -fprofile-instr-generate -fcoverage-mapping main.cpp -o main
	LLVM_PROFILE_FILE="main.profraw" ./main < kites.txt
	llvm-profdata merge -sparse main.profraw -o main.profdata
	llvm-cov show ./main -instr-profile=main.profdata