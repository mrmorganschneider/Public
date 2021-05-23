#! /usr/bin python

#generate a pickle dict file for export

import shelve
import os

def db_gen(path):
	dir_database = shelve.open('dir_database.db', 'c')
	
	dir_database['home'] = path
	dir_database['offline'] = ""
	dir_database['segy'] = ""
	dir_database['total_check'] = ""
	dir_database['fast_track'] = ""
	dir_database['edits'] = ""
	dir_database['p190'] =""

	dir_database.close()

	file_database = shelve.open('file_database.db' , 'c')

	file_database['QC_segd'] =""
	file_database['QC_cpsegd'] =""
	file_database['QC_nav'] =""
	file_database['QC_wr_segy'] =""
	file_database['QC_chksegy'] =""
	file_database['QC_cubeprep'] =""
	file_database['QC_brtstk'] =""
	file_database['Total_Check'] =""
	file_database['decon_cube'] =""
	file_database['denoise'] =""
	file_database['radon_g1'] =""
	file_database['radon_g2'] =""
	file_database['navmerge'] =""

	file_database.close()
