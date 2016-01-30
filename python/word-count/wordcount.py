from string import punctuation
import re

def word_count(string):
	r = re.compile(r'[\s{}]+'.format(re.escape(punctuation)))
	words = r.split(string)
	count = {}
	for word in words:
		if word.lower() not in count:
			count[word.lower()] = 1
		else:
			count[word.lower()]+=1
	count.pop("", None)
	return count