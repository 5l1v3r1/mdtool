
# imports

import os
import sys
import time
import random

# defs

def errorcheck():
	if ecount == 1:
		print('ERROR: ', usrinput, ' Please restart the tool, or if it is occuring many times, then please contact the developer on this email : blue_matrixh@protonmail.com')
		time.sleep(4)
		return

def scriptplayg():
	print(' __  __ ____ _____           _ ')
	print('|  \/  |  _ \_   _|__   ___ | |')
	print('| |\/| | | | || |/ _ \ / _ \| |')
	print('| |  | | |_| || | (_) | (_) | |')
	print('|_|  |_|____/ |_|\___/ \___/|_|---> Welcome to MDTool Playground!')
	print('[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]')
	return

def change():
	if (startbox < 1):
		scriptplayg()

# main

os.system('clear')
print(' __  __ ____ _____           _                               ')
print('|  \/  |  _ \_   _|__   ___ | |    Welcome to MDTool > V5.3  ')
print('| |\/| | | | || |/ _ \ / _ \| | --> MADE BY Rivan Juthani <--')
print('| |  | | |_| || | (_) | (_) | | --> http://mdtool.com/<--')
print('|_|  |_|____/ |_|\___/ \___/|_| Please read README.md before use')
print('           ----> MDTool <:> MultiDoableTool <----               ')
print('[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]')
print('               STARTING THE TOOL... PLEASE BE CALM')
time.sleep(4)
os.system('clear')
startbox = 0
ecount = 0
while ecount == 0:
	errorcheck()
	change()
	startbox += 1
	usrinput = raw_input('[mdtoolusr@MDT-box]$ ')
	if usrinput == 'help':
		ecount = 0
		os.system('clear')
		print('----> Welcome to HELP BOX')
		print('	-->	Command : What it does')
		print('		help : Shows this help box')
		print('		sqlmap : Starts sqlmap on the playground')
		print('		speedtest : Show the internet;s speed on the playground')
		print('		exit : Exits the playground and the script; returns to the terminal')
		print('  Waiting 5 seconds')
		print('[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]')
		time.sleep(5)
	if usrinput == 'exit':
		ecount = 0
		os.system('clear')
		print(' __  __ ____ _____           _                               ')
		print('|  \/  |  _ \_   _|__   ___ | |    Welcome to MDTool > V5.3  ')
		print('| |\/| | | | || |/ _ \ / _ \| | --> MADE BY Rivan Juthani <--')
		print('| |  | | |_| || | (_) | (_) | | --> http://mdtool.com/<--')
		print('|_|  |_|____/ |_|\___/ \___/|_| Please read README.md before use')
		print('           ----> MDTool <:> MultiDoableTool <----               ')
		print('[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]')
		print('        BYE SEE YOU LATER, THANKS FOR USING OUR TOOL!')
		time.sleep(2)
		os.system('exit')
	if usrinput == 'speedtest':
		ecount = 0
		os.system('clear')
errorcheck()
