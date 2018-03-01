import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):

    # Tree view
    viewList = None

    # Buttons
    addWordB = None
    acceptB  = None
    refreshB = None
    selectImageB = None

    # Fields
    wordEntry = None
    hitsEntry = None
    wordSizeCombo = None

    infoLabel = Gtk.Label('Add words')

    def __init__(self,wordList):
        Gtk.Window.__init__(self,title = "Fallout Terminal")
               
        # Initialize list
        self.viewList = Gtk.TreeView(wordList)
        renderer = Gtk.CellRendererText()
        column   = Gtk.TreeViewColumn("Words",renderer,text=0)
        self.viewList.append_column(column)
        # Scroll list
        scroll_list = Gtk.ScrolledWindow()
        scroll_list.add(self.viewList)

        # Interface building
        self.addWordB     = Gtk.Button(label = "Add")
        self.acceptB      = Gtk.Button(label = "Filter")
        self.refreshB     = Gtk.Button(label = "Clean")
        self.selectImageB = Gtk.Button(label = "Text recognition")
        self.wordEntry = Gtk.Entry()
        self.hitsEntry = Gtk.Entry()

        comboList = Gtk.ListStore(int)
        self.wordSizeCombo = Gtk.ComboBox.new_with_model(comboList)
        cell = Gtk.CellRendererText()
        self.wordSizeCombo.pack_start(cell, True)
        self.wordSizeCombo.add_attribute(cell, "text", 0)

        for t in (4,5,6,7,8,9,10,11,12,13,14,15):
            comboList.append((t,))

        # Initial configuration
        self.selectImageB.set_sensitive(False)

        # Boxes
        # Text recognition
        textRec_hb = Gtk.HBox()
        textRec_hb.pack_start(Gtk.Label("Size for OCR:"),True,True,2)
        textRec_hb.pack_start(self.wordSizeCombo,True,True,2)
        textRec_hb.pack_start(self.selectImageB,True,True,2)

        # Adding words
        newWords_hb = Gtk.HBox()
        newWords_hb.pack_start(self.wordEntry,True,True,2)
        newWords_hb.pack_start(self.addWordB,True,True,2)
        # Word Hits
        hits_hb = Gtk.HBox()
        hits_hb.pack_start(Gtk.Label("Hits:"),False,True,2)
        hits_hb.pack_start(self.hitsEntry,True,True,2)
        hits_hb.pack_start(self.acceptB,True,True,2)
        # Vertical
        vb = Gtk.VBox()
        vb.pack_start(textRec_hb,False,False,2)
        vb.pack_start(Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL),False,False,2)
        vb.pack_start(newWords_hb,False,False,2)
        vb.pack_start(scroll_list,True,True,2)
        vb.pack_start(hits_hb,False,False,2)
        vb.pack_start(self.refreshB,False,False,2)
        vb.pack_start(self.infoLabel,False,False,2)


        self.add(vb)
        self.set_border_width(5)
        self.set_default_size(600,400)
        self.connect("delete-event",Gtk.main_quit)                
        self.show_all()