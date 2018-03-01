import re

# Simple class to parse text from Fallout Terminal screenshot and get a word array
class TerminalTextParser(object):

	# Get a word array from terminal text
	@staticmethod
	def parse_text(text):
		# Eliminating spaces, end of lines, ROBCOINDUSTRIES and LEFT:
		mainText = text.replace("\n","").replace(" ","").replace("ROBCOINDUSTRIES","").replace("LEFT:","")
		# Find words
		wlist    = re.findall(r'(?<![O|Ox|OxF|A-Z|0-9])[A-Z]{4,15}(?![O|Ox|OxF|A-Z|0-9])',mainText,re.MULTILINE)

		return wlist  