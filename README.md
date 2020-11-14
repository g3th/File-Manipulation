# File-Manipulation

## Various scripts to manipulate files on either Windows or Linux.

**Note:** *These scripts were created to move downloaded movies/series for Plex.*

### Moviemove

Creates a folder named after the movie which it contains, and it does this for every mp4 present in the current directory.

It's a tedious task to move every mp4 by hand; since Plex is specific about naming conventions, a new folder will need to be created, 
and the respective file will need to be moved into the appropriately named folder. Moviemove is used for this task.

### Fileutil

Moves multiple Series mp4s into the a directory created with the program. 

For instance, all files named "[S01E01]The Office.mp4, [S01E02]The Office.mp4" will be moved into "The Office/Season 01". 

### DoesitExist

Simply searches your Plex database, generated with Database.py, and determines whether a file is already present. This is used before picking movies/series to download.
This script will need two lists, serielist and movielist, in order to begin searches.

As you can see, these scripts were specifically written to automate everyday tasks, in this case actions taken repeatedly when downloading/sorting my Plex collection.
