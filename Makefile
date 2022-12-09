all:
	# make clean
	make directories
	cd ./bin/utils && ./cprint_header.sh
	cd ./bin/ && ./run.sh
run:
	cd ./bin/ && ./run.sh
clean:
	cd ./bin/ && ./clean.sh
setup:
	make directories
	cd ./bin/ && ./setup.sh
directories:
	cd ./bin/ && ./make_directories.sh
