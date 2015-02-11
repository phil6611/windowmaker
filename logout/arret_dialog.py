#!/usr/bin/python
# -*- coding: utf-8 -*-
# installer libclutter et "python gi"
#version 0.3 décembre 2013
#license GPL V3 

from gi.repository import Gtk
import sys, os, dbus

class arretDialog:
	def __init__(self):
		fichier = os.path.dirname(sys.argv[0]) + "./arret.glade"
		interface = Gtk.Builder()
		interface.add_from_file(fichier)
		interface.connect_signals(self)

	def on_mainWindow_destroy(self, widget):
		Gtk.main_quit()       
	def on_eteindre_clicked(self, button):
		bus = dbus.SystemBus()
		bus_object = bus.get_object("org.freedesktop.login1","/org/freedesktop/login1")
		bus_object.PowerOff(0, dbus_interface="org.freedesktop.login1.Manager")
	def on_veille_clicked(self, widget):
		bus = dbus.SystemBus()
		bus_object = bus.get_object("org.freedesktop.login1","/org/freedesktop/login1")
		bus_object.Suspend(0, dbus_interface="org.freedesktop.login1.Manager")
	def on_redemarrer_clicked(self, widget):
		bus = dbus.SystemBus()
		bus_object = bus.get_object("org.freedesktop.login1","/org/freedesktop/login1")
		bus_object.Reboot(0, dbus_interface="org.freedesktop.login1.Manager")	
	def on_annuler_clicked(self, widget):
		Gtk.main_quit()

if __name__ == "__main__":
	arretDialog()
	Gtk.main()
