def wordsTyping(sentence, rows, cols):
	s = ' '.join(sentence)+' '
	start, l = 0,len(s)

	for i in xrange(0, rows):
		start += cols
		if(s[start %l] == ' '):
			start += 1
		else:
			while(start >= 0 and s[(start-1) % l] != ' '):
				start -= 1
	return start/l

rows = 2
cols = 8
sentence = ["hello", "world"]
print(wordsTyping(sentence, rows, cols))
