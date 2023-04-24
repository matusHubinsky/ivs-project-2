###################################################################
#
# Name of the project: ivs project 2
#
###################################################################
#
# @file Makefile
# @brief Makefile for second project of ivs
#
# @date 03.04.2023
#
# @author Boris Hatala
#
# ##################################################################

PY = python3
PYTEST = pytest

ZIPNAME = xhubin04_xduric07_xhatal02

GUI = gui.py
TEST = test.py
PROFILING = stddev.py

#Option help prints usage of the Makefile
help:
	@echo "This is a simple calculator for Ubuntu 64bit"
	@echo "Usage: make OPTION"
	@echo "									 "
	@echo "Options:											  		 	"
	@echo "	help 		prints usage of the Makefile"
	@echo "	all 		compiles whole project including profiling"
	@echo "	pack 		zip whole project"
	@echo "	test 		run tests for math library"
	@echo "	run		runs calculator"
	@echo "	doc		compiles documentation of the project "
	@echo "	profile 	runs the program for calculation of decisive derivant for profiling	"
	@echo "	clean 		deletes all the files that are not neccessary for compiling   	  	"

#Option all download neccessary dependencies for running this project
all:
	sudo apt install python3-tk python3-pip && pip3 install lark pytest

#Option pack zips contents of the project for handing out
pack: clean doc
	rm -rf ../../$(ZIPNAME).zip ../../$(ZIPNAME)
	cd ../../ && mkdir $(ZIPNAME)
	cd .. && cp -r * ../$(ZIPNAME)/
	cd ../../ && zip -r $(ZIPNAME).zip $(ZIPNAME) 
	rm -rf ../../$(ZIPNAME)


#Option test runs tests for math library
test: $(TEST)
	 $(PYTEST) $^

#Option run runs the program
run: $(GUI)
	$(PY) $^

#Option doc generates documentation for the project
doc: clean 
	doxygen Doxyfile
	mv doc ..

#Option profile runs the program for calculation of decisive derivant for profiling
profile: $(PROFILING)
	@ $(PY) $^ *.txt
	
#Option clean removes all the files that have been created after compiling and are not needed for handing out the project
clean:
	rm -rf ./build 
	rm -rf ./dist
	rm -rf ../doc
	rm -f *.spec
	rm -f warning_doxygen.txt
	rm -rf __pycache__

.PHONY: all clean test profile run pack doc install
### End of file Makefile ###
