all: fuzzer coverage

fuzzer:
	chmod +x fuzz.py
	./fuzz.py

coverage:
	llvm-cov show ./main -instr-profile=profFiles/main.profdata main.cpp > coverage.txt

