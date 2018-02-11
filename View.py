import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):

    # Visualización de lista
    viewList = None

    # Botones
    addWordB = None
    acceptB  = None
    refreshB = None

    # Campos
    wordEntry = None
    hitsEntry = None

    infoLabel = Gtk.Label('Añade las palabras')

    def __init__(self,wordList):
        Gtk.Window.__init__(self,title = "Fallout Terminal")
               
        # Inicialización Lista
        self.viewList = Gtk.TreeView(wordList)
        renderer = Gtk.CellRendererText()
        column   = Gtk.TreeViewColumn("Palabra",renderer,text=0)
        self.viewList.append_column(column)
        # Lista con scroll
        scroll_list = Gtk.ScrolledWindow()
        scroll_list.add(self.viewList)

        # Construcción de la interfaz
        self.addWordB  = Gtk.Button(label = "Añadir")
        self.acceptB   = Gtk.Button(label = "Comprobar")
        self.refreshB  = Gtk.Button(label = "Limpiar")
        self.wordEntry = Gtk.Entry()
        self.hitsEntry = Gtk.Entry()

        # Cajas de la ventana
        # Horizontal para añadir palabras
        newWords_hb = Gtk.HBox()
        newWords_hb.pack_start(self.wordEntry,True,True,2)
        newWords_hb.pack_start(self.addWordB,True,True,2)
        # Horizontal para hits de palabras
        hits_hb = Gtk.HBox()
        hits_hb.pack_start(Gtk.Label("Aciertos:"),False,True,2)
        hits_hb.pack_start(self.hitsEntry,True,True,2)
        hits_hb.pack_start(self.acceptB,True,True,2)
        # Vertical
        vb = Gtk.VBox()        
        vb.pack_start(newWords_hb,False,False,2)
        vb.pack_start(scroll_list,True,True,2)
        vb.pack_start(hits_hb,False,False,2)
        vb.pack_start(self.refreshB,False,False,2)
        vb.pack_start(self.infoLabel,False,False,2)

        self.add(vb)
        self.set_border_width(5)
        self.set_default_size(600,400)
        # Conectores propios de la vista (no hay interacción con el modelo)
        self.connect("delete-event",Gtk.main_quit)                
        # Mostar IU
        self.show_all()

class DialogoAdvertencia():

    def __init__(self,titulo,mensaje,parent):
        dialogo = Gtk.Dialog(titulo,parent,0,(Gtk.STOCK_OK,Gtk.ResponseType.OK))
        dialogo.get_content_area().add(Gtk.Label(mensaje))
        dialogo.show_all()
        dialogo.run()
        dialogo.destroy()