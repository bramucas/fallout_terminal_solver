import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

from Model.WordList import WordList
from View.MainWindowHandler  import MainWindowHandler


## Initlize model and view
modelList = WordList()
handler = MainWindowHandler(modelList)
Gtk.main()
