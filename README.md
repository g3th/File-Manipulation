# File-Manipulation

## Various scripts to manipulate files on either Windows or Linux.

**Note:** *These scripts were created to move downloaded movies/series for Plex.*

Examples:

It's a tedious task to move every mp4 by hand; a new folder will need to be created, since Plex is specific about naming conventions,
and the respective files will need to be each moved into an appropriately named folder. Moviemove is used for this task.

The same is true for series, where a folder will need to be created with the series name and subfolders created for each season. fileutil is used for this task.

Doesitexist will search your Plex database and determine whether a file is already present. This is used before picking movies/series to download.
This script will need two lists, serielist and movielist, in order to begin searches; both can be generated with Database.py

As you can see, these scripts were specifically written to automate everyday tasks, in this case actions taken repeatedly when downloading/sorting my Plex collection.
