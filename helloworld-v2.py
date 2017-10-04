#!/usr/bin/python
# $Id$

import argparse
import sys

def usage ():
    print( 'Command can be run with --v for verbose' )

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output')
    parser.add_argument('-v', dest='verbose', action='store_true')
    args = parser.parse_args()
    # ... do something with args.output ...
    # ... do something with args.verbose ..

# first line, print a silly string
print( 'Hello, World! My name is Maria.' )

print( '\n\n' )			# a couple of spaces to make it readable

# now show the number thingie-bob
num = 36			# set the variable 'num' value to 36
print( num )			# and print the variable 'num'

quit()
