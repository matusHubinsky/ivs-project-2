###################################################################
#
#Name of the project: ivs project 2
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

ZIPNAME = xhubin04_xduric07_xhatal02
ZIPFILES = ${shell cd ..} ${shell cd..} ${shell ls}

#Option all compiles whole project also profiling
all: $(EXECUTABLE) 

$(EXECUTABLE): core.py gui.py
	$(PY) $(PYFLAGS) $^

#Option pack packs-up contents of the project for handing out
pack: *.py Makefile
	cd .. && zip -r $(ZIPNAME) *

#Option test runs tests for math library
test:
	 $(PYTEST) $@

#Option run runs the program
run: guy.py core.py
	$(PY) $^

#Option doc generates documentation for the project
doc:
	doxygen Doxyfile

#Option profile runs the program for calculation of decisive derivant for/of profiling
profile:


#Option clean removes all the files that have been created after compiling and are not needed for handing out the project
clean:
	rm -r $(EXECUTABLE) 

.PHONY: clean

### End of file Makefile ###
