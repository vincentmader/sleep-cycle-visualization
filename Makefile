all:
	# make clean
	make directories
	make run
run:
	cd ./bin/utils && ./cprint_header.sh
	cd ./bin && ./run.sh
setup:
	make directories
	cd ./bin/ && ./setup.sh
directories:
	cd ./bin/ && ./make_directories.sh
clean:
	cd ./bin/ && ./clean.sh
