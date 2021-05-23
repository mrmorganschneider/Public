#!/usr/bin python

#launch edit calculator

import pygtk
pygtk.require('2.0')
import gtk
import os
import shelve
import shutil


class edit_calc:

	def close_edit_calc(self, widget, data=None):

		self.edit_calc_window.destroy()

	def msp_toggle(self, widget, msp, state):

		msp.set_editable(state)

	def calculate(self, widget, file_name, edit_fgsp, edit_lgsp, edit_fchan, edit_lchan, edit_msp, yes_button):
                
		file = file_name.get_text()
		fgsp = edit_fgsp.get_text() 
		lgsp = edit_lgsp.get_text() 
		fchan = edit_fchan.get_text()
		lchan = edit_lchan.get_text() 
		msp = edit_msp.get_text()

		dir_config = shelve.open('dir_database.db', 'r')
		src = dir_config['edits'] +file
		dst_dir = dir_config['home'] + "/edits/" 
		dst = dst_dir +file

		algo = './algo %s %s %s %s %s' % (file, fgsp, lgsp, fchan, lchan)
		
		print algo

		shutil.copyfile(src, dst)

		os.chdir(dst_dir)

		if (yes_button.get_active()):
			algo = algo + " -m %s" %msp
	
		os.system(algo)

		os.remove(dst)

		home_dir = dir_config['home']

		os.chdir(home_dir)

		dir_config.close()

	def edit_calculator(self, widget):

		dir_config = shelve.open('dir_database.db', 'r')

		self.edit_calc_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.edit_calc_window.set_title("Edit Calculator")
		self.edit_calc_window.connect("delete_event", self.close_edit_calc)
		self.edit_calc_window.set_border_width(10)
		self.edit_calc_window.set_destroy_with_parent(True)

		edit_box = gtk.VBox(False, 0)

		edit_entry_box = gtk.HBox(False, 0)

		edit_entry = gtk.Entry()
                edit_entry.set_max_length(20)
                edit_entry.set_width_chars(20)

		edit_entry_box.pack_start(edit_entry, False, False, 0)

		edit_entry_sep = gtk.HSeparator()
		edit_entry_box.pack_start(edit_entry_sep, False, True, 5)

		edit_entry_label = gtk.Label("Enter edit file name here")
		edit_entry_box.pack_start(edit_entry_label, False, False, 0)

		edit_box.pack_start(edit_entry_box, False, True, 5)

		edit_fgsp_box = gtk.HBox(False, 0)

                edit_fgsp = gtk.Entry()
                edit_fgsp.set_max_length(4)
                edit_fgsp.set_width_chars(15)

                edit_fgsp_box.pack_start(edit_fgsp, False, False, 0)

                edit_fgsp_sep = gtk.HSeparator()
                edit_fgsp_box.pack_start(edit_fgsp_sep, False, True, 5)

                edit_fgsp_label = gtk.Label("Enter first good shot point here")
                edit_fgsp_box.pack_start(edit_fgsp_label, False, False, 0)

                edit_box.pack_start(edit_fgsp_box, False, True, 5)

		edit_lgsp_box = gtk.HBox(False, 0)

                edit_lgsp = gtk.Entry()
                edit_lgsp.set_max_length(4)
                edit_lgsp.set_width_chars(15)

                edit_lgsp_box.pack_start(edit_lgsp, False, False, 0)

                edit_lgsp_sep = gtk.HSeparator()
                edit_lgsp_box.pack_start(edit_lgsp_sep, False, True, 5)

                edit_lgsp_label = gtk.Label("Enter last good shot point here")
                edit_lgsp_box.pack_start(edit_lgsp_label, False, False, 0)

                edit_box.pack_start(edit_lgsp_box, False, True, 5)

		edit_fchan_box = gtk.HBox(False, 0)

                edit_fchan = gtk.Entry()
                edit_fchan.set_max_length(5)
                edit_fchan.set_width_chars(15)

                edit_fchan_box.pack_start(edit_fchan, False, False, 0)

                edit_fchan_sep = gtk.HSeparator()
                edit_fchan_box.pack_start(edit_fchan_sep, False, True, 5)

                edit_fchan_label = gtk.Label("Enter first channel here")
                edit_fchan_box.pack_start(edit_fchan_label, False, False, 0)

                edit_box.pack_start(edit_fchan_box, False, True, 5)

		edit_lchan_box = gtk.HBox(False, 0)

                edit_lchan = gtk.Entry()
                edit_lchan.set_max_length(5)
                edit_lchan.set_width_chars(15)

                edit_lchan_box.pack_start(edit_lchan, False, False, 0)

                edit_lchan_sep = gtk.HSeparator()
                edit_lchan_box.pack_start(edit_lchan_sep, False, True, 5)

                edit_lchan_label = gtk.Label("Enter last channel here")
                edit_lchan_box.pack_start(edit_lchan_label, False, False, 0)

                edit_box.pack_start(edit_lchan_box, False, True, 5)
	
		msp_label = gtk.Label("Enter missed shot points here:")
                edit_msp = gtk.Entry()
		edit_msp.set_editable(False)
                edit_msp.set_width_chars(24)


		radio_box = gtk.HBox(False, 10)
		
		radio_label = gtk.Label("Are there any missed shots?")
		radio_box.pack_start(radio_label, False, False, 0)

		button_box = gtk.HBox(True, 0)

		radio_button1 = gtk.RadioButton(None, "No")
		radio_button1.connect("toggled", self.msp_toggle, edit_msp, False)
		button_box.pack_end(radio_button1, False, True, 0)
		
		radio_button2 = gtk.RadioButton(radio_button1, "Yes")
		radio_button2.connect("toggled", self.msp_toggle, edit_msp, True)
		button_box.pack_start(radio_button2, False, True, 0)

		radio_box.pack_start(button_box, False, False, 0)

		edit_box.pack_start(radio_box, False, True, 5)
		edit_box.pack_start(msp_label, False, False, 0)
                edit_box.pack_start(edit_msp, False, True, 5)

		end_box = gtk.HBox(True, 5)

                calc_button=gtk.Button("Calculate")
                calc_button.connect("clicked", self.calculate, edit_entry, edit_fgsp, edit_lgsp, edit_fchan, edit_lchan, edit_msp, radio_button2)
                close_button=gtk.Button("Close", gtk.STOCK_CLOSE)
                close_button.connect("clicked", self.close_edit_calc)

                end_box.pack_start(calc_button, False, False, 0)

                end_box.pack_start(close_button, False, False, 0)

		edit_box.pack_start(end_box, False, False, 0)

		self.edit_calc_window.add(edit_box)
		self.edit_calc_window.show_all()
