###################################################################
#
#Name of the project:  
#
###################################################################
#
# @file Makefile
# @brief This is a Makefile for second project of ivs
#
# @date 11.03.2023
#
# @author Matúš Hubinský
# @author Adam Ďurica
# @author Boris Hatala
#
# ##################################################################

PY = python3
PYTEST = pytest
PYFLAGS = 

EXECUTABLE=calculator

ZIPNAME = xhubin04_xduric07_xhatal02.zip

#Option help prints usage of the Makefile
help:
	@echo "Usage: make OPTION																"
	@echo "															  					  	"
	@echo "Options:											  						  	  	"
	@echo "	help 		prints usage of the Makefile											"
	@echo "	all 		compiles whole project including profiling						  	"
	@echo "	pack 		zip whole project 						  						  	"
	@echo "	test 		run tests for math library					  					  	"
	@echo "	run		runs calculator								  					  	"
	@echo "	doc		compiles documentation of the project		  					  	"
	@echo "	profile 	runs the program for calculation of decisive derivant for profiling	"
	@echo "	clean 		deletes all the files that are not neccessary for compiling   	  	"

#Option all compiles whole project also profiling
all: core.py gui.py
	$(PY) $(PYFLAGS) $^

#Option pack packs-up contents of the project for handing out
pack:
	cd .. && zip -r $(ZIPNAME) *

#Option test runs tests for math library
test: test.py
	 $(PYTEST) $^

#Option run runs the program
run: gui.py
	$(PY) $^

#Option doc generates documentation for the project
doc:
	doxygen Doxyfile

#Option profile runs the program for calculation of decisive derivant for profiling
profile:
	$(PY) $^

#Option clean removes all the files that have been created after compiling and are not needed for handing out the project
clean:
	rm -r $(EXECUTABLE) 

.PHONY: clean

### End of file Makefile ###
