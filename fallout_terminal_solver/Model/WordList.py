from Model.IncorrectWordSizeException import IncorrectWordSizeException

# Just control the word list
class WordList(object):

	wordList = None
	size 	 = None

	def __init__(self):
		self.size = None

	def setWordList(self, wordList):
		self.wordList = wordList

	def setSize(self, size):
		self.size = size

	# Return false if the new word have different size, True in another case
	def add(self, word):
		# First word to be added will set the size
		if (self.size == None):
			self.size = len(word)

		if (self.size != len(word)):
			raise IncorrectWordSizeException("Atention. '" + word + "' size doesn't match with current words size.")

		self.wordList.append([word])

	# Delete all words in the list wich not match with hits 
	def filter(self, word, hits):
		def compare(word1, word2):
			hits = 0
			for i in range(0,len(word1)):
				if (word1[i] == word2[i]):
					hits = hits + 1
			return hits

		for row in self.wordList:
			wordHits = compare(row[0],word)
			if (row[0] == word or wordHits != hits):
				self.wordList.remove(row.iter)

	def clean(self):
		self.size = None
		self.wordList.clear()