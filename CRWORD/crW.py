def createWords(n):	
	import random
	massWord = []
	word = ''
	i = 0

	for count in range(n):
		for count_word in range(6):
			while i < 6:
				word += chr(random.randint(65, 123))
				i += 1
		massWord += [word]
		word = ''
		i = 0
	return massWord

