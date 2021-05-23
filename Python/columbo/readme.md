# Columbo script launcher

Created by Morgan Schneider 2013

## Overview

This application was created by me to provide a single location for geophysical personnel onboard Polarcus vessels to find and display our various script and log outputs. Over time, many different scripts and log files were added to the systems onboard the vessels without much care given to their location or formatting. This application addresses this issue by storing the location and options for all the various scripts and log files needed to perform out daily tasks.

## Technical

The script makes heavy use of the pygtk library to create a GUI that is fairly intuitive and easy to use. The GUI includes a dropdown menu from where selections can be made. In addition to displaying log files, the application is also designed to launch scripts on the local system using calls to the os library as well as the ability to save and edit files on the local system. 

The program also makes extensive use of the shelve, shutl, and pickle libraries to store and retrieve file and script locations on the local system. This allowed users to edit and save the directories for the file locations on their respective vessels as these locations were often not standardized. The file locations are stored in a local db file called "dir_database.db", which in reality was just a pickle file rather than a true databse as developing a true database for the amount of data required for the program to operate would have been unnecessary.

## Notes
