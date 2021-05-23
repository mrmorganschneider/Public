#!/usr/bin python

#offline window creation

import pygtk
pygtk.require('2.0')
import gtk
import shelve
import os

class offline_window:

	def close_offline_window(self, widget, data=None):
		self.offline_window.destroy()
	
	def offline_script_call(self, widget, dir_data, file_data, home_dir): #program to call scripts in the offline directory
              
		os.chdir(dir_data)
               	filename = dir_data +file_data
               	os.system(filename)
		os.chdir(home_dir)

	def offline_window_call(self,widget):
	
		dir_config = shelve.open('dir_database.db', 'r')
		file_config = shelve.open('file_database.db', 'r')

		self.offline_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.offline_window.connect("delete_event", self.close_offline_window)
		self.offline_window.set_border_width(10)
		self.offline_window.set_title("Offline scripts")
		self.offline_window.set_default_size(200, -1)
		self.offline_window.set_destroy_with_parent(True)

		offline_box = gtk.VBox(True, 0)

		re_segd_button = gtk.Button("Read Segd") #create and show read segd button
               	re_segd_button.connect("clicked", self.offline_script_call, dir_config['offline'], file_config['QC_segd'], dir_config['home'])
               	offline_box.pack_start(re_segd_button, True, False, 5)

               	cp_segd_button = gtk.Button("Copy Segd") #create and show copy segd button
               	cp_segd_button.connect("clicked", self.offline_script_call, dir_config['offline'], file_config['QC_cpsegd'], dir_config['home'])
               	offline_box.pack_start(cp_segd_button, True, False, 5)

               	navmerge_button = gtk.Button("Navmerge") #create and show navmerge button
               	navmerge_button.connect("clicked", self.offline_script_call, dir_config['offline'], file_config['QC_nav'], dir_config['home'])
               	offline_box.pack_start(navmerge_button, True, False, 5)

		separator = gtk.HSeparator()
		offline_box.pack_start(separator, False, True, 5)

		close_box = gtk.HBox(False, 0)
		close_button = gtk.Button("Close", gtk.STOCK_CLOSE)
		close_button.connect("clicked", self.close_offline_window)
		
		close_box.pack_end(close_button, False, False, 0)
		offline_box.pack_start(close_box, False, False, 0)

		self.offline_window.add(offline_box)
		self.offline_window.show_all()

		dir_config.close()
		file_config.close() 
