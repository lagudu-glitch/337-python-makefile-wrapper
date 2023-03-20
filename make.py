#!/usr/bin/env python3

import subprocess, sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def check_arc_latch (fname):
	with open(fname, 'r') as fp:
		for l_no, line in enumerate (fp):
			if 'latch' in line:
				print(bcolors.FAIL + " !!!! LATCHES IN DESIGN !!!! " + line.split()[1] + " is a latch" + bcolors.ENDC)
			elif 'timing arc' in line:
				print(bcolors.FAIL + " !!!! TIMING ARC IN DESIGN !!!!" + bcolors.ENDC)


if __name__ == "__main__":
	if (len(sys.argv) != 5 or sys.argv[1] == "-help" or sys.argv[1] == "-h"):
		print ("""
************************************************************************************************\n
Author: Vishnu Lagudu
Make sure that command has five arguments
make.py is included in the five arguments.\n
************************************************************************************************\n
Syntax     : 	    ./make.py -<Modes of compilation> -<Types of compilation> -top <TOP MODULE>
Example    :        ./make.py -full -mapped -t top
-help / -h :	    Describes how this script works\n
************************************************************************************************\n
Modes of compilation\n
-full 	   :        Compiles a design with mutiple component files
-indv 	   : 	    Compiles indvidual modules with testbench\n
************************************************************************************************\n
Types of compilation\n
-source	   :        Simulates source version of design.
-mapped	   :        Simulates mapped version of design.\n
************************************************************************************************\n
TOP MODULE\n
-t                : Necessary argument
<top module name> : Name of your top module
		""")
		sys.exit()

	fname = sys.argv[4] + ".log"

	if (sys.argv[1] == "-full"):
		if (sys.argv[2] == "-source"):
			subprocess.call ("make sim_full_source", shell=True)

		elif (sys.argv[2] == "-mapped"):
			subprocess.call ("make sim_full_mapped", shell=True)

			check_arc_latch (fname)


	elif (sys.argv[1] == "-indv"):
		if (sys.argv[2] == "-source"):
			cmd = "make tbsim_" + sys.argv[4] + "_source"
			subprocess.call (cmd, shell=True)
		
		elif (sys.argv[2] == "-mapped"):
			cmd = "make tbsim_" + sys.argv[4] + "_mapped"
			subprocess.call (cmd, shell=True)

			check_arc_latch (fname)
