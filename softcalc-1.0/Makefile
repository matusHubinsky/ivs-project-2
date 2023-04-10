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
PYINSTALL = pyinstaller
PYTEST = pytest
INSFLAGS = -m -0755

DESTDIR = $(HOME)
ZIPNAME = xhubin04_xduric07_xhatal02.zip

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

#Option all compiles whole project also profiling
all: softcalc 

softcalc: core.py
	pyi-makespec $^.py
	pyinstaller core.spec


#Option pack packs-up contents of the project for handing out
pack:
	@echo "Creating a zip file $(ZIPNAME)"
	cd .. && zip -r $(ZIPNAME) *

#Option test runs tests for math library
test: $(TEST)
	 $(PYTEST) $^

#Option run runs the program
run: $(GUI)
	$(PY) $^

#Option doc generates documentation for the project
doc:
	doxygen Doxyfile
	cd doc && make

#Option profile runs the program for calculation of decisive derivant for profiling
profile: $(PROFILING)

#Option clean removes all the files that have been created after compiling and are not needed for handing out the project
clean:
	rm -rf ./build 
	rm -rf ./dist
	rm -f *.spec
	rm -rf doc warning_doxygen.txt
	rm -f __pycache__

install: softcalc
	mkdir -p $(DESTDIR)/opt
	cd dist; find kufr -type f -exec install -D $(INSFLAGS) "{}" "$(DESTDIR)/opt/{}" \;

.PHONY: all clean test profile run pack doc install
### End of file Makefile ###
