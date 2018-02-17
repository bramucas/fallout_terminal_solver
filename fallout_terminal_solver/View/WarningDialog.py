import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class WarningDialog():

    def __init__(self,titulo,mensaje,parent):
        dialogo = Gtk.Dialog(titulo,parent,0,(Gtk.STOCK_OK,Gtk.ResponseType.OK))
        dialogo.get_content_area().add(Gtk.Label(mensaje))
        dialogo.show_all()
        dialogo.run()
        dialogo.destroy()