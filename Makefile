all: main test

main: main.cpp
	clang++ -c main.cpp
	clang++ -o main main.o

test: main
	chmod +x test.sh
	./test.sh

coverage:
	clang++ -fprofile-instr-generate -fcoverage-mapping main.cpp -o main
	LLVM_PROFILE_FILE="main.profraw" ./main < test.txt
	llvm-profdata merge -sparse main.profraw -o main.profdata
	llvm-cov show ./main -instr-profile=main.profdata