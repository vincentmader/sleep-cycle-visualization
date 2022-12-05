all:
	cd ./bin/utils && ./cprint_header.sh
	cd ./bin/ && ./clean.sh
	cd ./bin/ && ./run.sh
run:
	cd ./bin/ && ./run.sh
clean:
	cd ./bin/ && ./clean.sh
setup:
	cd ./bin/ && ./setup.sh
