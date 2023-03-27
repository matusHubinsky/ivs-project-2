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

PY = python

FLAGS = 

MAIN = test.py, gui.py

GUI = gui.py


#Option all compiles whole project also profiling
all:
	$(PY) $(FLAGS) $(MAIN)

#Option pack packs-up contents of the project for handing out
pack:
	zip xhubin04_xduric07_xhatal02.zip $(MAIN)

#Option test runs tests for math library
test:
	pytest test.py

#Option run runs the program
run:
	$(PY) $(GUI)

#Option doc generates documentation for the project
doc:
	doxygen Doxyfile

#Option profile runs the program for calculation of decisive derivant for/of profiling
profile:


#Option clean removes all the files that have been created after compiling and are not needed for handing out the project
clean:
	rm -rf 


















### End of file Makefile ###
