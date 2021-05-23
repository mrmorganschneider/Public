#!/usr/bin python

#fast track window creation

import pygtk
pygtk.require('2.0')
import gtk
import os
import shelve

class fast_track_window:

	def close_fast_track_window(self, widget, data=None):
		self.fast_track_window.destroy()
	
	def fast_track_script_call(self, widget, dir_data, file_data, home_dir): #program to call scripts in the fast track directory
              
		os.chdir(dir_data)
		os.system("clear")
               	filename = dir_data +file_data
               	os.system(filename)
		os.chdir(home_dir)

	def fast_track_window_call(self,widget):

		dir_config = shelve.open('dir_database.db', 'r')
                file_config = shelve.open('file_database.db', 'r')

		self.fast_track_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.fast_track_window.connect("delete_event", self.close_fast_track_window)
		self.fast_track_window.set_border_width(10)
		self.fast_track_window.set_title("Fast Track scripts")
		self.fast_track_window.set_default_size(200, -1)
		self.fast_track_window.set_destroy_with_parent(True)

		fast_track_box = gtk.VBox(True, 0)

		decon_button = gtk.Button("Decon Cube") #create and show read decon button
               	decon_button.connect("clicked", self.fast_track_script_call, dir_config['fast_track'], file_config['decon_cube'], dir_config['home'])
               	fast_track_box.pack_start(decon_button, True, False, 5)

               	denoise_button = gtk.Button("Denoise") #create and show denoise button
               	denoise_button.connect("clicked", self.fast_track_script_call, dir_config['fast_track'], file_config['denoise'], dir_config['home'])
               	fast_track_box.pack_start(denoise_button, True, False, 5)

               	radon_g1_button = gtk.Button("Radon g1") #create and show navmerge button
               	radon_g1_button.connect("clicked", self.fast_track_script_call, dir_config['fast_track'], file_config['radon_g1'], dir_config['home'])
               	fast_track_box.pack_start(radon_g1_button, True, False, 5)

               	radon_g2_button = gtk.Button("Radon g2") #create and show navmerge button
               	radon_g2_button.connect("clicked", self.fast_track_script_call, dir_config['fast_track'], file_config['radon_g2'], dir_config['home'])
               	fast_track_box.pack_start(radon_g2_button, True, False, 5)

               	navmerge_button = gtk.Button("Navmerge") #create and show navmerge button
               	navmerge_button.connect("clicked", self.fast_track_script_call, dir_config['fast_track'], file_config['navmerge'], dir_config['home'])
               	fast_track_box.pack_start(navmerge_button, True, False, 5)

		separator = gtk.HSeparator()
		fast_track_box.pack_start(separator, False, True, 5)

		close_box = gtk.HBox(False, 0)
		close_button = gtk.Button("Close", gtk.STOCK_CLOSE)
		close_button.connect("clicked", self.close_fast_track_window)
		
		close_box.pack_end(close_button, False, False, 0)
		fast_track_box.pack_start(close_box, False, False, 0)

		self.fast_track_window.add(fast_track_box)
		self.fast_track_window.show_all() 

		dir_config.close()
		file_config.close()
