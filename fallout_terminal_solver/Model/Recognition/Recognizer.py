from PIL import Image
import sys

import pyocr
import pyocr.builders

from Model.Recognition.TerminalTextParser import TerminalTextParser
from Model.Recognition.NoOCRToolsException import NoOCRToolsException

# Encapsulate text recognition funcionality
class Recognizer(object):

	tool = None

	def __init__(self):
		tools = pyocr.get_available_tools()
		if len(tools) == 0:
			raise NoOCRToolsException("No hay herramientas OCR instaladas o no están disponible en el PATH.")
		self.tool = tools[0]

	def text_from_image(self, imageRoute):
		return self.tool.image_to_string(Image.open(imageRoute),
			builder=pyocr.builders.TextBuilder())

	def parse_terminal_text(self, text):
		return TerminalTextParser.parse_text(text)

	def terminalImage_to_wordArray(self, imageRoute):
		return self.parse_terminal_text(self.text_from_image(imageRoute))
