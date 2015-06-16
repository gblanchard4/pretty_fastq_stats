#! /usr/bin/env python
 
import argparse
 
__author__ = "Gene Blanchard"
__email__ = "me@geneblanchard.com"
 
'''
Pretty Fastq Stats
'''
 
def main():
	#  Argument Parser
	parser = argparse.ArgumentParser(description='Generate some nice looking fastq stats about read length and truncation')
 
	# Input file
	parser.add_argument('-i','--input',dest='input', help='The input fastq')
	# Output file
	parser.add_argument('-o','--output',dest='output', help='The output file')
	
	# Parse arguments
	args = parser.parse_args()
	infile = args.input
	outfile = args.output
 
    # Do stuff here 
 
if __name__ == '__main__':
	main()