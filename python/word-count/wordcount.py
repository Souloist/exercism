from string import punctuation
import re

def word_count(string):
	r = re.compile(r'[\s{}]+'.format(re.escape(punctuation))) # filtering out punctuation
	words = r.split(string) # list of words

	count = {} # dict containing word count

	for word in words:

		# adds word into dict with value 1 if word is not in dict
		if word.lower() not in count:
			count[word.lower()] = 1
		
		# increments the key value if the word is already a key
		else:
			count[word.lower()]+=1

	count.pop("", None) # removing empty string key from dict
	return count