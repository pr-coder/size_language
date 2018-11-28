import sys
sys.path.append("C:\\Users\\User\\Desktop\\file\\CRWORD")
import os

import crW

english_words = crW.createWords(134000)

file_of_words = open('english.txt', 'w')
sys.stdout = file_of_words
for string in english_words:
	print (string, end='')
size_english_words = os.path.getsize('english.txt')
print ("\n\n\tSize words equally " + str((float(size_english_words) / 1024.0) / 1024.0))

#os.path.getsize
file_of_words.close()
