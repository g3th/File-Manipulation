#!/usr/bin/python3

import glob

#Easy movie list
#from both drives

n=0;movies=[]
pathm=["/mounted/Media/Movies/*","/mounted1/Media/Movies/*"]
paths=["/mounted/Media/Tv Shows/*","/mounted1/Media/TV Shows/*"]
opt=str(input("(1) Movies list (2) Series List: "))
if opt =="1":
	path=pathm
	listfile="Movielist"
else:
	path=paths
	listfile="Serieslist"
while n<2:
	for files in glob.glob(path[n]):
		movies.append(str(files).split("/")[4])
	n=n+1
sort=sorted(movies)
with open(listfile,'a+') as mr:
	for lines in sort:
		mr.write(str(lines)+"\n")
	if listfile=="Serieslist":
		mr.write("\nTotal Number of Series: "+str(len(movies)))
	else:
		mr.write("\nTotal Number of Movies: "+str(len(movies)))
