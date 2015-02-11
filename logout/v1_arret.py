#!/usr/bin/python
# -*- coding: utf-8 -*-
# installer libclutter et "python gi"
#version 0.1 décembre 2013
#license GPL V3

from gi.repository import Gtk
import os

class arretDialog:
    def __init__(self):
        interface = Gtk.Builder()
        interface.add_from_file('arret.glade')
        
        self.myLabel = interface.get_object("myLabel")
        interface.connect_signals(self)

    def on_mainWindow_destroy(self, widget):
        Gtk.main_quit()       
    def on_eteindre_clicked(self, button):
	os.system("shutdown")
    def on_veille_clicked(self, widget):
	os.system("ls")
    def on_redemarrer_clicked(self, widget):
	os.system("ls")
    def on_annuler_clicked(self, widget):
	Gtk.main_quit()

if __name__ == "__main__":
    arretDialog()
    Gtk.main()