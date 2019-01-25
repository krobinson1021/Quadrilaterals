all: main

main: main.cpp
	gcc -O main.cpp -std=c99 -o main

test: main
	./test.sh

cover:
	clang++ -fprofile-instr-generate -fcoverage-mapping main.cpp -o main
	LLVM_PROFILE_FILE="main.profraw" ./main < kites.txt
	llvm-profdata merge -sparse main.profraw -o main.profdata
	llvm-cov show ./main -instr-profile=main.profdata