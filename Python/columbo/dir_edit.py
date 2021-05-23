#! /usr/bin python

import pygtk
pygtk.require('2.0')
import gtk
import os
import shelve

class dir_edit_window:

	def destroy_window(self, widget):

                self.edit_window.destroy()

        def save_dir_edits(self, widget):

                save_dialog = gtk.Dialog("Confirm", self.edit_window, 
			gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                        (gtk.STOCK_OK, 1, gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT))

		save_label = gtk.Label("This will overwrite the current values. Continue?")
		save_dialog.vbox.pack_start(save_label)
		save_dialog.show_all()
                response = save_dialog.run()

                if (response == 1):

			print "Saving..."

			dir_config = shelve.open('dir_database.db', 'w')

			#set dictionary values to entries
                        dir_config['offline'] = self.offline_entry.get_text()
                        dir_config['segy'] = self.segy_entry.get_text()
                        dir_config['total_check'] = self.total_entry.get_text()
                        dir_config['fast_track'] = self.fast_entry.get_text()
                        dir_config['edits'] = self.edits_entry.get_text()
                        dir_config['p190'] = self.p190_entry.get_text()

			#save offline entries to pkl file
			dir_config.close()

                save_dialog.destroy()

	def dir_edit_call(self, widget, data = None):

		dir_config = shelve.open('dir_database.db', 'r')

		#Edit window constructors
             	self.edit_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
                self.edit_window.set_title( "Edit Directories" )
                self.edit_window.set_border_width(10)
		self.edit_window.set_transient_for(self.main_window)
		self.edit_window.set_modal(True)
	
		#creates main vertical box
                edit_vbox = gtk.VBox(False, 0)
		
		#create offline entry box
		offline_box = gtk.HBox(False, 0)
		
		
		#create offline entry box for user text	
                self.offline_entry = gtk.Entry()
                self.offline_entry.set_text(dir_config['offline'])
		self.offline_entry.set_max_length(75)
		self.offline_entry.set_width_chars(75)

                offline_box.pack_start(self.offline_entry, False, False, 0)

		offline_sep = gtk.HSeparator()
		offline_box.pack_start(offline_sep, False, True, 5)
		
		#create offline label
		offline_label = gtk.Label("Enter Offline directory here")
		offline_box.pack_start(offline_label, False, False, 0)
		
		#pack offline box			
		edit_vbox.pack_start(offline_box, False, True, 5)
		
		
		#create segy entry box
		segy_box = gtk.HBox(False, 0)
		
		#create segy entry box for user text	
               	self.segy_entry = gtk.Entry()
                self.segy_entry.set_text(dir_config['segy'])
		self.segy_entry.set_max_length(75)
		self.segy_entry.set_width_chars(75)

                segy_box.pack_start(self.segy_entry, False, False, 0)

		segy_sep = gtk.HSeparator()
		segy_box.pack_start(segy_sep, False, True, 5)
		
		#create segy label
		segy_label = gtk.Label("Enter Segy directory here")
		segy_box.pack_start(segy_label, False, False, 0)
		
		#pack offline box			
		edit_vbox.pack_start(segy_box, False, True, 5)
		
		
		#create total check entry box
		total_check_box = gtk.HBox(False, 0)
		
		#create total check entry box for user text	
                self.total_entry = gtk.Entry()
                self.total_entry.set_text(dir_config['total_check'])
		self.total_entry.set_max_length(75)
		self.total_entry.set_width_chars(75)

                total_check_box.pack_start(self.total_entry, False, False, 0)

		total_sep = gtk.HSeparator()
		total_check_box.pack_start(total_sep, False, True, 5)
		
		#create total check label
		total_label = gtk.Label("Enter Total Check directory here")
		total_check_box.pack_start(total_label, False, False, 0)
		
		#pack total check box			
		edit_vbox.pack_start(total_check_box, False, True, 5)
		
		
		#create fast track entry box
		fast_track_box = gtk.HBox(False, 0)
		
		#create fast track entry box for user text	
                self.fast_entry = gtk.Entry()
                self.fast_entry.set_text(dir_config['fast_track'])
		self.fast_entry.set_max_length(75)
		self.fast_entry.set_width_chars(75)

                fast_track_box.pack_start(self.fast_entry, False, False, 0)

		fast_sep = gtk.HSeparator()
		fast_track_box.pack_start(fast_sep, False, True, 5)
		
		#create fast track label
		fast_label = gtk.Label("Enter Fast Track directory here")
		fast_track_box.pack_start(fast_label, False, False, 0)
		
		#pack offline box			
		edit_vbox.pack_start(fast_track_box, False, True, 5)
		
		#create edit files entry box
		edits_box = gtk.HBox(False, 0)
		
		#create fast track entry box for user text	
                self.edits_entry = gtk.Entry()
                self.edits_entry.set_text(dir_config['edits'])
		self.edits_entry.set_max_length(75)
		self.edits_entry.set_width_chars(75)

                edits_box.pack_start(self.edits_entry, False, False, 0)

		edits_sep = gtk.HSeparator()
		edits_box.pack_start(edits_sep, False, True, 5)
		
		#create fast track label
		edits_label = gtk.Label("Enter edit file directory here")
		edits_box.pack_start(edits_label, False, False, 0)
		
		#pack fast track box			
		edit_vbox.pack_start(edits_box, False, True, 5)

		p190_box = gtk.HBox(False, 0)
		
		#create p190 entry box for user text	
                self.p190_entry = gtk.Entry()
                self.p190_entry.set_text(dir_config['p190'])
		self.p190_entry.set_max_length(75)
		self.p190_entry.set_width_chars(75)

                p190_box.pack_start(self.p190_entry, False, False, 0)

		p190_sep = gtk.HSeparator()
		p190_box.pack_start(p190_sep, False, True, 5)
		
		#create p190 label
		p190_label = gtk.Label("Enter p190 file directory here")
		p190_box.pack_start(p190_label, False, False, 0)
		
		#pack p190 box			
		edit_vbox.pack_start(p190_box, False, True, 5)

		end_separator = gtk.HSeparator()
                end_separator.set_size_request(400, 10)
                edit_vbox.pack_start(end_separator, False, True, 10)
		
		#create save and close
		end_box = gtk.HBox(True, 5)
		
                save_button=gtk.Button("Save",gtk.STOCK_SAVE)
                save_button.connect("clicked", self.save_dir_edits)
                close_button=gtk.Button("Close", gtk.STOCK_CLOSE)
                close_button.connect("clicked", self.destroy_window)

                end_box.pack_start(save_button, False, False, 0)

                end_box.pack_start(close_button, False, False, 0)
                
		edit_vbox.pack_start(end_box, False, False, 0)

		#add main edit box to edit window
		self.edit_window.add(edit_vbox)
                self.edit_window.show_all()

		dir_config.close()
