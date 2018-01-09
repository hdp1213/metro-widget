#!/usr/bin/env python
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GdkPixbuf

class TrayIcon(Gtk.StatusIcon):
    def __init__(self):
        Gtk.StatusIcon.__init__(self)
        self.set_from_file('/usr/share/icons/gnome/16x16/emotes/face-cool.png')
        self.set_has_tooltip(True)
        self.set_visible(True)
        self.connect("activate", self.on_primary_click)
        self.connect("popup_menu", self.on_secondary_click)


    def on_primary_click(self, widget):
        event = Gtk.get_current_event()
        btn = event.button #this gets the button value of gtk event.
        time = Gtk.get_current_event_time()

        menu = Gtk.Menu()

        menu_item1 = Gtk.MenuItem()

        vbox = Gtk.VBox(False)
        vbox.pack_start(Gtk.Label('test'), expand=False, fill=True, padding=0)

        menu_item1.add(vbox)

        menu.append(menu_item1)

        menu.show_all()
        menu.popup(None, None, None, self, btn.type, time)

    def on_secondary_click(self, widget, button, time):
        menu = Gtk.Menu()

        menu_item1 = Gtk.MenuItem('Settings')
        menu.append(menu_item1)

        menu_item2 = Gtk.MenuItem('Quit')
        menu.append(menu_item2)
        menu_item2.connect('activate', Gtk.main_quit)

        menu.show_all()
        menu.popup(None, None, None, self, 1, time)

    def do_activate(self):
        pass
        
if __name__ == '__main__':
    win = TrayIcon()
    Gtk.main()

