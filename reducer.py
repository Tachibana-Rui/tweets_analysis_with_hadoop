#!/usr/bin/env python3

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
	for line in file:
		yield line.rstrip().split(separator, 1)

def main(separator='\t'):
	# input comes from STDIN (standard input)
	data = read_mapper_output(sys.stdin, separator=separator)
	# groupby groups multiple word-count pairs by word,
	# and creates an iterator that returns consecutive keys and their group:
	#   current_word - string containing a word (the key)
	#   group - iterator yielding all ["&lt;current_word&gt;", "&lt;count&gt;"] items
	for current_word, group in groupby(data, itemgetter(0)):
		try:
			total_count = sum(int(count) for current_word, count in group)
			print(current_word+separator+str(total_count))
		except ValueError:
			# count was not a number, so silently discard this item
			pass

def test(separator='\t'):
	map_output = open(r'map_output.txt','r',encoding='utf-8')
	data = read_mapper_output(map_output, separator=separator)
	for current_word, group in groupby(data, itemgetter(0)):
		try:
			total_count = sum(int(count) for current_word, count in group)
			print(current_word+separator+str(total_count))
		except ValueError:
			# count was not a number, so silently discard this item
			pass

if __name__ == "__main__":
#	test()
	main()