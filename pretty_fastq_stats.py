#! /usr/bin/env python
 
import argparse
from Bio import SeqIO
from collections import OrderedDict

__author__ = "Gene Blanchard"
__email__ = "me@geneblanchard.com"
 
'''
Pretty Fastq Stats
'''
# def parse_fastq(filename):
# 	file = open(filename)
# 	sequence_length = None
# 	five = None
# 	ten = None
# 	fifteen = None
# 	twenty = None
# 	for i,line in enumerate(file):
# 		if i % 4 == 1:
# 			current_sequence = line.rstrip('\n')
# 		if i % 4 == 3:
# 			qualities = [ord(x) - 33 for x in line.rstrip('\n')]
# 			five = qualities.index(5)
# 			ten = qualities.index(10)
# 			fifteen = qualities.index(15)
# 			twenty = qualities.index(20)
# 		yield(sequence_length, five, ten, fifteen, twenty)


def process_dict_value(value, dictionary):
	try:
		dictionary[value] += 1
	except KeyError:
		dictionary[value] = 1
	return dictionary

def percentify(number):
	 return "{0:.1f}%".format(number)


def main():
	# Argument Parser
	parser = argparse.ArgumentParser(description='Generate some nice looking fastq stats about read length and truncation')
 
	# Input file
	parser.add_argument('-i','--input',dest='input', help='The input fastq', required=True)
	# Output file
	parser.add_argument('-o','--output',dest='output', help='The output file')
	
	# Parse arguments
	args = parser.parse_args()
	infile = args.input
	outfile = args.output

	# Dictionaries to hold out stats
	length_dict = {}
	five = {}
	ten = {}
	fifteen = {}
	twenty = {}

	# Read the fastq
	with open(infile, "rU") as handle:
		for record in SeqIO.parse(handle, "fastq"):
			
			# Length Processing
			sequence_length = len(record.seq)
			length_dict = process_dict_value(sequence_length, length_dict)

			# if sequence_length in length_dict:
			# 	# Increment sequence count
			# 	length_dict[sequence_length] += 1
			# else:
			# 	length_dict[sequence_length] = 1

			# Quality processing
			quality_list = record.letter_annotations['phred_quality']
			# Q5
			try:
				five = process_dict_value(quality_list.index(5), five)
			except ValueError:
				pass

			# Q10
			try:
				ten = process_dict_value(quality_list.index(10), ten)
			except ValueError:
				pass
			# Q15
			try:
				fifteen = process_dict_value(quality_list.index(15), fifteen)
			except ValueError:
				pass
			# Q20
			try:
				twenty = process_dict_value(quality_list.index(20), twenty)
			except ValueError:
				pass

	# Order the dictionaries
	length_dict = OrderedDict(sorted(length_dict.items(), key=lambda t: t[0]))
	five = OrderedDict(sorted(five.items(), key=lambda t: t[0]))
	ten = OrderedDict(sorted(ten.items(), key=lambda t: t[0]))
	fifteen = OrderedDict(sorted(fifteen.items(), key=lambda t: t[0]))
	twenty = OrderedDict(sorted(twenty.items(), key=lambda t: t[0]))

	#OUTPUT
	# Length
	print "Length Dict: {}".format(len(length_dict.keys()))
	length_sum = sum(length_dict.itervalues())
	accum_percent = 0
	for key in length_dict:
		percent = float(length_dict[key])/float(length_sum) * 100
		accum_percent += percent
		print key, length_dict[key], percentify(percent),  percentify(100-accum_percent)
	# 5
	print "5: {}".format(len(five.keys()))
	five_sum = sum(five.itervalues())
	accum_percent = 0
	for key in five:
		percent = float(five[key])/float(five_sum) * 100
		accum_percent += percent
		print key, five[key], percentify(percent), percentify(accum_percent)
	# 10
	print "10 Dict: {}".format(len(ten.keys()))
	ten_sum = sum(ten.itervalues())
	accum_percent = 0
	for key in ten:
		percent = float(ten[key])/float(ten_sum) * 100
		accum_percent += percent
		print key, ten[key], percentify(percent), percentify(accum_percent)
	# 15 
	print "15 Dict: {}".format(len(fifteen.keys()))
	fifteen_sum = sum(fifteen.itervalues())
	accum_percent = 0
	for key in fifteen:
		percent = float(fifteen[key])/float(fifteen_sum) * 100
		accum_percent += percent
		print key, fifteen[key], percentify(percent), percentify(accum_percent)
	# 20
	print "20 Dict: {}".format(len(twenty.keys()))
	twenty_sum = sum(twenty.itervalues())
	accum_percent = 0
	for key in twenty:
		percent = float(twenty[key])/float(twenty_sum) * 100
		accum_percent += percent
		print key, twenty[key], percentify(percent), percentify(accum_percent)





 
if __name__ == '__main__':
	main()