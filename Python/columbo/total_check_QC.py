#!/usr/bin python

#offline window creation

import pygtk
pygtk.require('2.0')
import gtk
import shelve
import os

class total_check:

	def total_check_call(self, widget): #program to call scripts in the offline directory
              
		dir_config = shelve.open('dir_database.db', 'r')
		file_config = shelve.open('file_database.db', 'r')

		os.chdir(dir_config['total_check'])
               	filename = dir_config['total_check'] +file_config['Total_Check']
               	os.system(filename)
		os.chdir(dir_config['home'])
		
		dir_config.close()
		file_config.close() 
