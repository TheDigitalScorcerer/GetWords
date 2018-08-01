# Words from http://www.allscrabblewords.com

def getWordsByLetterNum(letters, outputfile="", separator="\n"):
	import os
	import urllib.request
	letters = str(letters)

	response = urllib.request.urlopen("http://www.allscrabblewords.com/" + letters + "-letter-words")
	html = response.read()

	text = str(html).split("<ul class=\"list-inline\">")[-1]
	text = text.split("</ul>")[0]
	text = text.replace("<li>", "").replace("</li>", "").replace("<a title=\"Unscramble ", "").replace(" | Words made by unscrambling the letters in ", "").replace(" | Word Decoder for ", "").replace("\" href=\"/word-description/", "").replace("\">", "").replace("/a>", "")

	wordlist = []
	for piece in text.split("<   "):
		newpiece = ""
		for letter in range(int(letters)):
			newpiece += piece.replace(" ", "")[letter]
		wordlist.append(newpiece)

	if outputfile:
		f = open(outputfile, "w+")
		for word in wordlist:
			f.write(word + separator)
		f.close()

	return wordlist

