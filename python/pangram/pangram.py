def is_pangram(sentence):
	alphabet = "abcdefghijklmnopqrstuvwxyz"

	for letter in range(len(alphabet)):
		if alphabet[letter] not in sentence.lower(): # Check in case sentence has uppercase letters
			return False
	return True