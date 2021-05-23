#! /usr/bin python

#calculation scripts

import pygtk
pygtk.require('2.0')
import gtk
import re
import os
import shelve

class awkp190:
	
	def close_p190_window(self, widget):
		self.p190_window.destroy()

	def run_awkp190(self, widget):

		dir_config = shelve.open("dir_database.db")

		os.chdir(dir_config['p190'])

		for filename in os.listdir(dir_config['p190']):
        		if re.search(".p190$", filename):
                		zedit_filepath = dir_config['p190'] + filename + ".zedit"
                		if not os.path.isfile(zedit_filepath) and not (filename == "awkp190"):		
					command = "awkp190 %s > %s.zedit" %(filename, filename)

					print command

					os.system(command)

		os.chdir(dir_config['home'])

		self.p190_window.destroy()

		success_dialog = gtk.Dialog("Success", self.p190_window,
                gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
               	(gtk.STOCK_OK, gtk.RESPONSE_REJECT))

                success_label = gtk.Label("All zedit files created successfully")
                success_dialog.vbox.pack_start(success_label)
                success_dialog.show_all()
               	response = success_dialog.run()
		success_dialog.destroy()

		self.p190_window.destroy()

		dir_config.close()

	def start_awkp190(self, widget):

		self.p190_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.p190_window.connect ("delete_event", self.close_p190_window)
		self.p190_window.set_border_width(10)
		self.p190_window.set_title("Run awkp190 script")
		self.p190_window.set_default_size(-1, -1)
		self.p190_window.set_destroy_with_parent(True)

		p190_box = gtk.VBox(False, 0)

		p190_label = gtk.Label("Execute awkp190 script?")
		p190_box.pack_start(p190_label, False, True, 5)

		end_separator = gtk.HSeparator()
                end_separator.set_size_request(400, 10)
                p190_box.pack_start(end_separator, False, True, 10)

                #create save and close
                end_box = gtk.HBox(True, 5)

                ok_button=gtk.Button("Run",gtk.STOCK_OK)
                ok_button.connect("clicked", self.run_awkp190)
                close_button=gtk.Button("Close", gtk.STOCK_CLOSE)
                close_button.connect("clicked", self.close_p190_window)

                end_box.pack_end(close_button, False, False, 0)

                end_box.pack_end(ok_button, False, False, 0)

                p190_box.pack_start(end_box, True, True, 0)

		self.p190_window.add(p190_box)
		self.p190_window.show_all()

		
