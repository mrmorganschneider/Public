#! /usr/bin python

import os
import pygtk
pygtk.require('2.0')
import gtk
import shelve

class file_edit_window:

	def destroy_window(self, widget):

                self.edit_window.destroy()

        def save_file_edits(self, widget):

		save_dialog = gtk.Dialog("Confirm", self.edit_window, 
			gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                        (gtk.STOCK_OK, 1, gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT))

		save_label = gtk.Label("This will overwrite the current file names. Continue?")
		save_dialog.vbox.pack_start(save_label)
		save_dialog.show_all()
                response = save_dialog.run()

                if (response == 1):

			print "Saving..."

			file_config = shelve.open('file_database.db', 'w')

			#set dictionary values to entries
                        file_config['QC_segd'] = self.segd_entry.get_text()
                        file_config['QC_cpsegd'] = self.cpsegd_entry.get_text()
                        file_config['QC_nav'] = self.nav_entry.get_text()
                        file_config['QC_wr_segy'] = self.wrsegy_entry.get_text()
                        file_config['QC_chksegy'] = self.chksegy_entry.get_text()
                        file_config['QC_cubeprep'] = self.cubeprep_entry.get_text()
                        file_config['QC_brtstk'] = self.brtstk_entry.get_text()
                        file_config['Total_Check'] = self.total_entry.get_text()
                        file_config['decon_cube'] = self.decon_entry.get_text()
                        file_config['denoise'] = self.denoise_entry.get_text()
                        file_config['radon_g1'] = self.radon_g1_entry.get_text()
                        file_config['radon_g2'] = self.radon_g2_entry.get_text()
                        file_config['navmerge'] = self.navmerge_entry.get_text()

			#save file entries to pkl file
			file_config.close()

                save_dialog.destroy()

	def file_edit_call(self, widget, data = None):

		file_config = shelve.open('file_database.db', 'r')

		#Edit window constructors
             	self.edit_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
                self.edit_window.set_title( "Edit File Names" )
                self.edit_window.set_border_width(10)
		self.edit_window.set_transient_for(self.main_window)
		self.edit_window.set_modal(True)
	
		#creates main vertical box
                edit_vbox = gtk.VBox(False, 0)
		
		#COPY 24 lines here
		#create segd entry box
		segd_box = gtk.HBox(False, 0)
		
		
		#create segd entry box for user text	
                self.segd_entry = gtk.Entry()
                self.segd_entry.set_text(file_config['QC_segd'])
		self.segd_entry.set_max_length(20)
		self.segd_entry.set_width_chars(20)

                segd_box.pack_start(self.segd_entry, False, False, 0)

		segd_sep = gtk.HSeparator()
		segd_box.pack_start(segd_sep, False, True, 5)
		
		#create segd label
		segd_label = gtk.Label("Enter write segd QC file here")
		segd_box.pack_start(segd_label, False, False, 0)
		
		#pack segd box			
		edit_vbox.pack_start(segd_box, False, True, 5)
		
		
		#create cpsegd entry box
		cpsegd_box = gtk.HBox(False, 0)
		
		#create cpsegd entry box for user text	
               	self.cpsegd_entry = gtk.Entry()
                self.cpsegd_entry.set_text(file_config['QC_cpsegd'])
		self.cpsegd_entry.set_max_length(20)
		self.cpsegd_entry.set_width_chars(20)

                cpsegd_box.pack_start(self.cpsegd_entry, False, False, 0)

		cpsegd_sep = gtk.HSeparator()
		cpsegd_box.pack_start(cpsegd_sep, False, True, 5)
		
		#create cpsegd label
		cpsegd_label = gtk.Label("Enter copy segd QC file here")
		cpsegd_box.pack_start(cpsegd_label, False, False, 0)
		
		#pack cpsegd box			
		edit_vbox.pack_start(cpsegd_box, False, True, 5)
		
		
		#create QC nav entry box
		nav_box = gtk.HBox(False, 0)
		
		#create nav entry box for user text	
                self.nav_entry = gtk.Entry()
                self.nav_entry.set_text(file_config['QC_nav'])
		self.nav_entry.set_max_length(20)
		self.nav_entry.set_width_chars(20)

                nav_box.pack_start(self.nav_entry, False, False, 0)

		nav_sep = gtk.HSeparator()
		nav_box.pack_start(nav_sep, False, True, 5)
		
		#create nav label
		nav_label = gtk.Label("Enter nav QC file here")
		nav_box.pack_start(nav_label, False, False, 0)
		
		#pack nav box			
		edit_vbox.pack_start(nav_box, False, True, 5)
		
		
		#create write segy entry box
		wrsegy_box = gtk.HBox(False, 0)
		
		#create write segy entry box for user text	
                self.wrsegy_entry = gtk.Entry()
                self.wrsegy_entry.set_text(file_config['QC_wr_segy'])
		self.wrsegy_entry.set_max_length(20)
		self.wrsegy_entry.set_width_chars(20)

                wrsegy_box.pack_start(self.wrsegy_entry, False, False, 0)

		wrsegy_sep = gtk.HSeparator()
		wrsegy_box.pack_start(wrsegy_sep, False, True, 5)
		
		#create write segy label
		wrsegy_label = gtk.Label("Enter write segy QC file here")
		wrsegy_box.pack_start(wrsegy_label, False, False, 0)
		
		#pack write segy box			
		edit_vbox.pack_start(wrsegy_box, False, True, 5)
		

		#create check segy files entry box
		chksegy_box = gtk.HBox(False, 0)
		
		#create check segy entry box for user text	
                self.chksegy_entry = gtk.Entry()
                self.chksegy_entry.set_text(file_config['QC_chksegy'])
		self.chksegy_entry.set_max_length(20)
		self.chksegy_entry.set_width_chars(20)

                chksegy_box.pack_start(self.chksegy_entry, False, False, 0)

		chksegy_sep = gtk.HSeparator()
		chksegy_box.pack_start(chksegy_sep, False, True, 5)
		
		#create check segy label
		chksegy_label = gtk.Label("Enter check segy QC file here")
		chksegy_box.pack_start(chksegy_label, False, False, 0)
		
		#pack check segy box			
		edit_vbox.pack_start(chksegy_box, False, True, 5)

	
		#create cubeprep entry box	
		cubeprep_box = gtk.HBox(False, 0)
		
		#create entry box for user text	
                self.cubeprep_entry = gtk.Entry()
                self.cubeprep_entry.set_text(file_config['QC_cubeprep'])
		self.cubeprep_entry.set_max_length(20)
		self.cubeprep_entry.set_width_chars(20)

                cubeprep_box.pack_start(self.cubeprep_entry, False, False, 0)

		cubeprep_sep = gtk.HSeparator()
		cubeprep_box.pack_start(cubeprep_sep, False, True, 5)
		
		#create label
		cubeprep_label = gtk.Label("Enter cubeprep QC file here")
		cubeprep_box.pack_start(cubeprep_label, False, False, 0)
		
		#pack box			
		edit_vbox.pack_start(cubeprep_box, False, True, 5)
		

		#create brute stack entry box
		brtstk_box = gtk.HBox(False, 0)
		
		#create entry box for user text	
                self.brtstk_entry = gtk.Entry()
                self.brtstk_entry.set_text(file_config['QC_brtstk'])
		self.brtstk_entry.set_max_length(20)
		self.brtstk_entry.set_width_chars(20)

                brtstk_box.pack_start(self.brtstk_entry, False, False, 0)

		brtstk_sep = gtk.HSeparator()
		brtstk_box.pack_start(brtstk_sep, False, True, 5)
		
		#create label
		brtstk_label = gtk.Label("Enter segy brute stack QC file here")
		brtstk_box.pack_start(brtstk_label, False, False, 0)
		
		#pack box			
		edit_vbox.pack_start(brtstk_box, False, True, 5)

		
		#create total check entry box
		total_box = gtk.HBox(False, 0)
		
		#create entry box for user text	
                self.total_entry = gtk.Entry()
                self.total_entry.set_text(file_config['Total_Check'])
		self.total_entry.set_max_length(20)
		self.total_entry.set_width_chars(20)

                total_box.pack_start(self.total_entry, False, False, 0)

		total_sep = gtk.HSeparator()
		total_box.pack_start(total_sep, False, True, 5)
		
		#create label
		total_label = gtk.Label("Enter total check file here")
		total_box.pack_start(total_label, False, False, 0)
		
		#pack box			
		edit_vbox.pack_start(total_box, False, True, 5)

		
		#create decon cube entry box
		decon_box = gtk.HBox(False, 0)
		
		#create entry box for user text	
                self.decon_entry = gtk.Entry()
                self.decon_entry.set_text(file_config['decon_cube'])
		self.decon_entry.set_max_length(20)
		self.decon_entry.set_width_chars(20)

                decon_box.pack_start(self.decon_entry, False, False, 0)

		decon_sep = gtk.HSeparator()
		decon_box.pack_start(decon_sep, False, True, 5)
		
		#create label
		decon_label = gtk.Label("Enter decon cube QC file here")
		decon_box.pack_start(decon_label, False, False, 0)
		
		#pack box			
		edit_vbox.pack_start(decon_box, False, True, 5)


		#create denoise entry box
		denoise_box = gtk.HBox(False, 0)
		
		#create entry box for user text	
                self.denoise_entry = gtk.Entry()
                self.denoise_entry.set_text(file_config['denoise'])
		self.denoise_entry.set_max_length(20)
		self.denoise_entry.set_width_chars(20)

                denoise_box.pack_start(self.denoise_entry, False, False, 0)

		denoise_sep = gtk.HSeparator()
		denoise_box.pack_start(denoise_sep, False, True, 5)
		
		#create label
		denoise_label = gtk.Label("Enter denoise QC file here")
		denoise_box.pack_start(denoise_label, False, False, 0)
		
		#pack box			
		edit_vbox.pack_start(denoise_box, False, True, 5)


		#create radon g1 entry box
		radon_g1_box = gtk.HBox(False, 0)
		
		#create entry box for user text	
                self.radon_g1_entry = gtk.Entry()
                self.radon_g1_entry.set_text(file_config['radon_g1'])
		self.radon_g1_entry.set_max_length(20)
		self.radon_g1_entry.set_width_chars(20)

                radon_g1_box.pack_start(self.radon_g1_entry, False, False, 0)

		radon_g1_sep = gtk.HSeparator()
		radon_g1_box.pack_start(radon_g1_sep, False, True, 5)
		
		#create label
		radon_g1_label = gtk.Label("Enter radon g1 QC file here")
		radon_g1_box.pack_start(radon_g1_label, False, False, 0)
		
		#pack box			
		edit_vbox.pack_start(radon_g1_box, False, True, 5)


		#create radon g2 entry box
		radon_g2_box = gtk.HBox(False, 0)
		
		#create entry box for user text	
                self.radon_g2_entry = gtk.Entry()
                self.radon_g2_entry.set_text(file_config['radon_g2'])
		self.radon_g2_entry.set_max_length(20)
		self.radon_g2_entry.set_width_chars(20)

                radon_g2_box.pack_start(self.radon_g2_entry, False, False, 0)

		radon_g2_sep = gtk.HSeparator()
		radon_g2_box.pack_start(radon_g2_sep, False, True, 5)
		
		#create label
		radon_g2_label = gtk.Label("Enter radon g2 QC file here")
		radon_g2_box.pack_start(radon_g2_label, False, False, 0)
		
		#pack box			
		edit_vbox.pack_start(radon_g2_box, False, True, 5)



		#create navmerge entry box
		navmerge_box = gtk.HBox(False, 0)
		
		#create entry box for user text	
                self.navmerge_entry = gtk.Entry()
                self.navmerge_entry.set_text(file_config['navmerge'])
		self.navmerge_entry.set_max_length(20)
		self.navmerge_entry.set_width_chars(20)

                navmerge_box.pack_start(self.navmerge_entry, False, False, 0)

		navmerge_sep = gtk.HSeparator()
		navmerge_box.pack_start(navmerge_sep, False, True, 5)
		
		#create label
		navmerge_label = gtk.Label("Enter fast track navmerge QC file here")
		navmerge_box.pack_start(navmerge_label, False, False, 0)
		
		#pack box			
		edit_vbox.pack_start(navmerge_box, False, True, 5)


		#create end seperator
		end_separator = gtk.HSeparator()
                end_separator.set_size_request(400, 10)
                edit_vbox.pack_start(end_separator, False, True, 10)
		
		#create save and close
		end_box = gtk.HBox(True, 5)
		
                save_button=gtk.Button("Save",gtk.STOCK_SAVE)
                save_button.connect("clicked", self.save_file_edits)
                close_button=gtk.Button("Close", gtk.STOCK_CLOSE)
                close_button.connect("clicked", self.destroy_window)

                end_box.pack_start(save_button, False, False, 0)

                end_box.pack_start(close_button, False, False, 0)
                
		edit_vbox.pack_start(end_box, False, False, 0)

		#add main edit box to edit window
		self.edit_window.add(edit_vbox)
                self.edit_window.show_all()
		
		file_config.close()
