#!/usr/bin python

#segy window creation

import pygtk
pygtk.require('2.0')
import gtk
import os
import shelve

class segy_window:

	def close_segy_window(self, widget, data=None):
		self.segy_window.destroy()
	
	def segy_script_call(self, widget, dir_data, file_data, home_dir): #program to call scripts in the segy directory
              
		os.chdir(dir_data)
               	filename = dir_data +file_data
               	os.system(filename)
		os.chdir(home_dir)

	def segy_window_call(self,widget):

		dir_config = shelve.open('dir_database.db', 'r')
                file_config = shelve.open('file_database.db', 'r')

		self.segy_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.segy_window.connect("delete_event", self.close_segy_window)
		self.segy_window.set_border_width(10)
		self.segy_window.set_title("Segy scripts")
		self.segy_window.set_default_size(200, -1)
		self.segy_window.set_destroy_with_parent(True)

		segy_box = gtk.VBox(True, 0)

		wr_segy_button = gtk.Button("Write Segy") #create and show read segd button
               	wr_segy_button.connect("clicked", self.segy_script_call, dir_config['segy'], file_config['QC_wr_segy'], dir_config['home'])
               	segy_box.pack_start(wr_segy_button, True, False, 5)
               	wr_segy_button.show()

               	chksegy_button = gtk.Button("Check Segy") #create and show copy segd button
               	chksegy_button.connect("clicked", self.segy_script_call, dir_config['segy'], file_config['QC_chksegy'], dir_config['home'])
               	segy_box.pack_start(chksegy_button, True, False, 5)
               	chksegy_button.show()

               	cubeprep_button = gtk.Button("Cubeprep") #create and show navmerge button
               	cubeprep_button.connect("clicked", self.segy_script_call, dir_config['segy'], file_config['QC_cubeprep'], dir_config['home'])
               	segy_box.pack_start(cubeprep_button, True, False, 5)
               	cubeprep_button.show()

               	brtstk_button = gtk.Button("Brute Stack") #create and show navmerge button
               	brtstk_button.connect("clicked", self.segy_script_call, dir_config['segy'], file_config['QC_brtstk'], dir_config['home'])
               	segy_box.pack_start(brtstk_button, True, False, 5)
               	brtstk_button.show()

		separator = gtk.HSeparator()
		segy_box.pack_start(separator, False, True, 5)

		close_box = gtk.HBox(False, 0)
		close_button = gtk.Button("Close", gtk.STOCK_CLOSE)
		close_button.connect("clicked", self.close_segy_window)
		
		close_box.pack_end(close_button, False, False, 0)
		segy_box.pack_start(close_box, False, False, 0)

		self.segy_window.add(segy_box)
		self.segy_window.show_all() 

		dir_config.close()
                file_config.close()

