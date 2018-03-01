import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

from View.MainWindow 	import MainWindow
from View.WarningDialog import WarningDialog

from Model.Recognition.Recognizer 		   import Recognizer
from Model.Recognition.NoOCRToolsException import NoOCRToolsException

from Model.IncorrectWordSizeException import IncorrectWordSizeException

# Connects view events with model functions
class MainWindowHandler(object):

	MainWindow = None
	ModelList  = None

	def __init__ (self,wordList):
		listStore = Gtk.ListStore(str)
		wordList.setWordList(listStore)
		self.ModelList = wordList
		self.MainWindow = MainWindow(listStore)
		# Conexiones
		self.MainWindow.selectImageB.connect("clicked", self.selectScreenshotAndGetWords)
		self.MainWindow.wordSizeCombo.connect("changed", self.onWordSizeComboChangeHandler)
		self.MainWindow.addWordB.connect("clicked", self.addNewWordHandler)
		self.MainWindow.wordEntry.connect("activate", self.addNewWordHandler)
		self.MainWindow.refreshB.connect("clicked", self.cleanListHandler)
		self.MainWindow.hitsEntry.connect("activate", self.filterHandler)
		self.MainWindow.acceptB.connect("clicked", self.filterHandler)

	# HANDLERS ------------------

	def addNewWordHandler(self,button):
		newWord = self.MainWindow.wordEntry.get_text()
		try:
			self.ModelList.add(newWord.upper())
			self.MainWindow.wordEntry.set_text("")
		except IncorrectWordSizeException as e:
			WarningDialog("Atention", e, self.MainWindow)			

	def filterHandler(self,button):
		model, it = self.MainWindow.viewList.get_selection().get_selected()
		if it == None:
			WarningDialog("Atention","Yo must select a word",self.MainWindow)
		else:
			word = model.get_value(it,0)
			hits = int(self.MainWindow.hitsEntry.get_text())
			self.ModelList.filter(word,hits)

	def cleanListHandler(self,button):
		self.ModelList.clean()

	def onWordSizeComboChangeHandler(self,combo):
		self.MainWindow.selectImageB.set_sensitive(True)

	# Allows user to choose an image and get words from it
	def selectScreenshotAndGetWords(self,button):
		# Choose image
		fileRoute = ""

		dialog = Gtk.FileChooserDialog("Please choose a file", self.MainWindow,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

		response = dialog.run()
		if response == Gtk.ResponseType.OK:
		    fileRoute = dialog.get_filename()
		dialog.destroy()
		
		if (fileRoute != ""):
			try:
				# Get words
				recognizer = Recognizer()
				words = recognizer.terminalImage_to_wordArray(fileRoute)

				# Update View
				incorrectWords = []
				self.ModelList.clean()

				# Set word size
				it = self.MainWindow.wordSizeCombo.get_active_iter()
				model = self.MainWindow.wordSizeCombo.get_model()
				size = model[it][0]
				self.ModelList.setSize(size)

				for s in words:
					try:
						self.ModelList.add(s.upper())
					except IncorrectWordSizeException as e:
						incorrectWords.append(s.upper())

				# Show recognition fails
				if (incorrectWords != []):
					WarningDialog("Atention","The following words didn't match: " + str(incorrectWords) ,self.MainWindow)
			except NoOCRToolsException as e:
				WarningDialog("Atention", e, self.MainWindow)

		