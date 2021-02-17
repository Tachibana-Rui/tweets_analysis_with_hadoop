#!/usr/bin python3

import sys
import json
import re

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
	# Dictionary of keyword appearance per tweet
	keywords = {'han':0,'hon':0,'den':0,'det':0,'denna':0,'denne':0,'hen':0}

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
			word = word.lower()
			if word in keywords.keys():
				keywords[word]+=1
		hit_keywords = filter(lambda x: 1 == x[1], keywords.items())

		if hit_keywords:
			for w in hit_keywords:
				print(w[0]+separator+str(1))
		#Set to default value
		keywords = {'han':0,'hon':0,'den':0,'det':0,'denna':0,'denne':0,'hen':0}

def test(separator='\t'):
	data = read_input(open(r'D:\Documents\UPPSALA\DataEngineering1\tweets_0.txt','r',encoding='utf-8'))
	map_output = open(r'map_output.txt','w',encoding='utf-8')
	# Dictionary of keyword appearance per tweet
	keywords = {'han':0,'hon':0,'den':0,'det':0,'denna':0,'denne':0,'hen':0}

	for words in data:
		# write the results to STDOUT (standard output);
		# what we output here will be the input for the
		# Reduce step, i.e. the input for reducer.py
		#
		# tab-delimited; the trivial word count is 1
		if not words:
			continue

		for word in words:
			word = word.lower()
			if word in keywords.keys():
				keywords[word]+=1

		hit_keywords = filter(lambda x: 1 == x[1], keywords.items())
		if hit_keywords:
			for w in hit_keywords:
				print(w[0]+separator+str(1),file=map_output)
		#Set to default value
		keywords = {'han':0,'hon':0,'den':0,'det':0,'denna':0,'denne':0,'hen':0}

if __name__ == "__main__":
#	test()
	main()