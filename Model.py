
class WordList(object):

	wordList = None
	size 	 = None

	def __init__(self,wordList):
		self.wordList = wordList
		self.size = None

	# Return false if the new word have different size, True in another case
	def add(self, word):
		# First word to be added will set the size
		if (self.size == None):
			self.size = len(word)

		if (self.size == len(word)):
			self.wordList.append([word])
			return True

		return False
# REVISAR LONGITUD PALABRAS

	def filter(self, word, hits):
		def compare(word1, word2):
			hits = 0
			for i in range(0,len(word1)):
				if (word1[i] == word2[i]):
					hits = hits + 1
			return hits

		for row in self.wordList:
			print(row[0])
			wordHits = compare(row[0],word)
			print("comparamos " + word + " con " + row[0] + ". Aciertos =" + str(wordHits))
			if (row[0] == word or wordHits != hits):
				print("vamoh a borrar " + row[0])
				self.wordList.remove(row.iter)

	def clean(self):
		self.wordList.clear()