import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

from View.MainWindow 	import MainWindow
from View.WarningDialog import WarningDialog

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
		self.MainWindow.addWordB.connect("clicked", self.addNewWordHandler)
		self.MainWindow.wordEntry.connect("activate", self.addNewWordHandler)
		self.MainWindow.refreshB.connect("clicked", self.cleanListHandler)
		self.MainWindow.hitsEntry.connect("activate", self.filterHandler)
		self.MainWindow.acceptB.connect("clicked", self.filterHandler)

	def addNewWordHandler(self,button):
		newWord = self.MainWindow.wordEntry.get_text()
		if (self.ModelList.add(newWord.upper()) == False):
			WarningDialog("Atención","La palabra que intentas añadir no se corresponde en tamaño con las demás",self.MainWindow)
		else:
			self.MainWindow.wordEntry.set_text("")

	def filterHandler(self,button):
		model, it = self.MainWindow.viewList.get_selection().get_selected()
		if it == None:
			WarningDialog("Atención","Antes debes seleccionar una palabra",self.MainWindow)
		else:
			word = model.get_value(it,0)
			hits = int(self.MainWindow.hitsEntry.get_text())
			self.ModelList.filter(word,hits)

	def cleanListHandler(self,button):
		self.ModelList.clean()