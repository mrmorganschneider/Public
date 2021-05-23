#! /usr/bin python

#starter script for Columbo

import pygtk
pygtk.require('2.0')
import os
import sys
import gtk
import db_gen

from columbo import Columbo

home_dir=os.path.dirname(sys.argv[0])
#print home
path=os.path.abspath(home_dir)

#print home

os.chdir(path)

if (sys.argv[1] == "install"):

	db_gen.db_gen(path)

if __name__ == '__main__':
    new_window = Columbo()
    gtk.main()

