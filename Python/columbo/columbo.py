#! /usr/bin python

### Columbo program management tool v.2 ###
### Created by Morgan Schneider ###

import pygtk
pygtk.require('2.0')
import gtk
import shelve

from dir_edit import dir_edit_window
from file_edit import file_edit_window
from offline_QC import offline_window
from segy_QC import segy_window
from total_check_QC import total_check
from fast_track_QC import fast_track_window
from edit_calc import edit_calc
from awkp190 import awkp190
#from print_txt_files import print_files

class Columbo(dir_edit_window, file_edit_window, offline_window, segy_window, total_check, fast_track_window, edit_calc, awkp190):
	
	#setup user interface
	ui = '''<ui>
	<menubar name = "MainMenu">
	 <menu action = "File">
	  <menuitem action = "Quit"/>
         </menu>
	 <menu action = "Edit">
	  <menuitem action = "Directory locations"/>
	  <menuitem action = "File names"/>
         </menu>
	 <menu action = "QC Scripts">
	  <menuitem action = "Offline"/>
	  <menuitem action = "Segy"/>
	  <menuitem action = "Total"/>
	  <menuitem action = "Fast"/>
	 </menu>
	 <menu action = "Calculations">
	  <menuitem action = "Edit calculator"/>
          <menuitem action = "Awk p190"/>
	 </menu>
	</menubar>
	</ui>'''

	def __init__(self):

		self.main_window = gtk.Window()
		self.main_window.connect('destroy', lambda w: gtk.main_quit())
		self.main_window.set_size_request(-1, -1)
		self.main_window.set_title("Columbo unified porgram launcher")
		self.main_window.set_resizable(False)

		vbox = gtk.VBox()
		self.main_window.add(vbox)

		interface = gtk.UIManager()
		accel_group = interface.get_accel_group()
		self.main_window.add_accel_group(accel_group)

		action_group = gtk.ActionGroup('Columbo')
		self.actiongroup = action_group

		#create menu actions for user interface
		action_group.add_actions ([('Quit', gtk.STOCK_QUIT, '_Quit', '<control>q', 'Quit the program', self.quit_program),
						('File', None, '_File'),
						('Directory locations', None,'_Directory locations', '<Control>d', 'Edit directory locations', self.dir_edit_call),
						('File names', None,'File _names', '<Control>n', 'Edit file names', self.file_edit_call),
						('Edit', None, '_Edit'),
						('Offline', None, '_Offline scripts', '<Control>o', 'Show Offline QC scripts', self.offline_window_call),
						('Segy', None, '_Segy scripts', '<Control>s', 'Show Segy QC scripts', self.segy_window_call),
						('Total', None, '_Total Check script', '<Control>t', 'Show Total Check output', self.total_check_call),
						('Fast', None, '_Fast Track scripts', '<Control>f', 'Show Fast Track QC scripts', self.fast_track_window_call),
						('QC Scripts', None, 'QC _Scripts'),
						('Edit calculator', None, 'Edit _Calculator', '<Control>c', 'Calculate a number of edits from a file', self.edit_calculator),
						('Awk p190', None, '_Awk p190', '<Control>a', 'Run awkp190 script on a file', self.start_awkp190),
						('Calculations', None, 'Calculations')])
		#				('Print files', None, 'Print weekly report files', None, None, self.print_window_call),
		#				('Print', None, 'Print')])

		action_group.get_action('Quit').set_property('short-label', '_Quit')

		interface.insert_action_group(action_group, 0)
		interface.add_ui_from_string(self.ui)

		menubar = interface.get_widget('/MainMenu')
		vbox.pack_start(menubar, False)

		front_image = gtk.Image()
		dir_config = shelve.open("dir_database.db")
		front_image_path = dir_config['home'] +"/columbo_front.jpg"
		front_image.set_from_file(front_image_path)
		vbox.pack_start(front_image)
		dir_config.close()

		self.main_window.show_all()
		return

	def quit_program(self, b):

		quit_dialog = gtk.Dialog("Quit Program", self.main_window, gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT, 
			(gtk.STOCK_YES, True, gtk.STOCK_NO, False))

		quit_label = gtk.Label("Exit Columbo program launcher?")
		quit_dialog.vbox.pack_start(quit_label, False, True, 5)
		quit_dialog.show_all()

		if quit_dialog.run():

        		print 'Quitting program'
        	
			gtk.main_quit()

		quit_dialog.destroy()

if __name__ == '__main__':
    ba = Columbo()
    gtk.main()

		
	
