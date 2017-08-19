def LetterChanges(s):
  '''
  Input: String
  Output: Each letter in the string has shifted down one letter in the alphabet.
  '''
	from string import ascii_letters
	news = ''
	for c in s:
		if c in ascii_letters:
			news = ns+ascii_letters[(ascii_letters.index(c)+1)%len(ascii_letters)]
		else:
			news+=c
	return news
print LetterChanges('Hello')
