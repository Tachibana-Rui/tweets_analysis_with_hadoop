import sys
import json
import re
import time

def read_input(file):
	temp={}
	for line in file:
		try:
			temp.clear()
			temp = json.loads(line)
			if not temp['retweet_count']:
				yield temp['text'].split()
			else:
				yield
		except: 
			yield


def main(separator='\t'):
	# input comes from STDIN (standard input)
	data = read_input(sys.stdin)
	for words in data:
		# write the results to STDOUT (standard output);
		# what we output here will be the input for the
		# Reduce step, i.e. the input for reducer.py
		#
		# tab-delimited; the trivial word count is 1
		if not words:
			continue
		for word in words:
			print(word+separator+str(1))

def test(separator='\t'):
	data = read_input(open(r'D:\Documents\UPPSALA\DataEngineering1\tweets_0.txt','r',encoding='utf-8'))
	map_output = open(r'map_output.txt','w',encoding='utf-8')
	for words in data:
		# write the results to STDOUT (standard output);
		# what we output here will be the input for the
		# Reduce step, i.e. the input for reducer.py
		#
		# tab-delimited; the trivial word count is 1
		if not words:
			continue
		for word in words:
			print(word+separator+str(1),file = map_output)

if __name__ == "__main__":
	main()
#	test()
