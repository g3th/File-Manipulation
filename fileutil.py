import glob, shutil, os, time
from os import system

system('cls');

directory= ''; validpath = 0; series_len = 0; filesfound = False

def Choice():
    print (" ______ _ _        _    _ _   _ _ ")
    print ("|  ____(_) |      | |  | | | (_) |")
    print ("| |__   _| | ___  | |  | | |_ _| |")
    print ("|  __| | | |/ _ \ | |  | | __| | |")
    print ("| |    | | |  __/ | |__| | |_| | |")
    print ("|_|    |_|_|\___|  \____/ \__|_|_|")
    if validpath ==1:
        print ("\n\n\n" + "Options: ")
        print ("1) File Search")
        print ("2) Move Files")
        print ("3) Set Path")
        print ("4) File List")
        print ("5) Quit")

def Set_Path():
    flag = 0
    while flag == False:
        dir__ = input ("\nEnter directory\n(format: C:/Media/Files/): ")
        ext_ = input("\nEnter file extension\n(format: txt, mp4, srt): ")
        file_list=[]; directory_ = dir__ + "*." +  ext_ 
        if file_list == 0:
             print ("\nNo Path Set. Try Again.")        
        for files in glob.glob(directory_):
             names = os.path.basename(files)
             file_list.append(names)         
        filelist_l= len(file_list)
        if filelist_l > 0:
            print ("\n" + "Got file list!" + " Found " + str(filelist_l) + " files." "\n")
            print (*file_list, sep="\n");input ("\nHit Enter...")
        else:
            print ("\nNo files returned."); input("\nHit Enter...")
        filesfound = True; flag = True
    return file_list, filelist_l, dir__, directory_, filesfound, ext_,

def File_Search():
        print("\nCurrent file type: " + ext + "\n")
        f_search_= input("\nEnter series or sub name\n(format: The Office, Stranger Things): ")
        season = input ("\nEnter season (format: 1, 2..):")
        filtered_ = dir_ + "[S" + season + ".E*" + f_search_ + "*" + ext
        series_list=[] 
        for series in glob.glob(filtered_):
            series_list.append(series)
            flag = True
        series_l= len(series_list)
        if series_l < 1:
            print("\nNo files returned.")
        else:
            print ("\n" + "Got file list!" + " Found " + str(series_l) + " files." "\n")
            print (*series_list, sep="\n")
        return series_list, f_search_, filtered_, series_l

def Move_Files():
        print ("\nThe series which will be moved is: " + filesearch +"\n")
        print ("\nThe path it will be moved to is: " + str(newdir) +"\n")
        correct = input ("\nIs this correct(y/n)? ")
        if correct == "y":
            for allfiles in glob.glob(str(filtered)):
                shutil.move(allfiles, newdir)

f=0; ctr=0
while f == False:
    Choice(); print("\n\nA valid path must be set \n")
    flist, flist_len, dir_, directory, filesfound, ext= Set_Path()
    validpath=1; f=1
    
while ctr ==False:
    system('cls'); Choice()
    option = input ("\nWhat would you like to do? ")
    if option == "1":
         series, filesearch, filtered, series_len = File_Search()
         input ("\nHit Enter...")
    if option == "2":
         system('cls')
         if series_len == 0:
             print ("\nThere is nothing stored. Returning.")
             input("\nHit Enter...")
         else:
             print ("\nThese are the files: \n"); print (*series, sep="\n")
             prompt= input ("\nWould you like to create a directory (y/n)? ")
             while True:
                 try:
                    if prompt == "y":
                        dir_name= input ("\nEnter partial new dir name\n(format: TV/subs/): ")   
                        path = os.path.join(dir_, dir_name)
                        newdir = os.makedirs(path); newdir = str(path)
                        print ("\nCreated '" + path + "' ")
                        break
                    else:
                        enterdir= input ("\nEnter full directory to move to\n(format: C:/Media/TV/..): ")
                        newdir = enterdir
                        break
                 except OSError:
                    print ("\n" + path + " already exists."),
                    there= input("Move there (y/n)?")
                    if there == "y":
                        newdir = path; break
             def_ = Move_Files()
    if option =="3":
        flist, flist_len, dir_, directory, filesfound, ext = Set_Path()    
    if option =="4":
        system('cls')
        fl=[]
        for f in glob.glob(directory):
            fl.append(f)
        if len(fl) ==0:
            print("\n\n\nCurrent path contains no files. \n")
        else:
            print("\n\n\nCurrent path contains: \n")
            print (*fl, sep="\n")
        input("\nHit Enter...")
    if option == "5":
        print("\nGoodbye.")
        time.sleep(2)
        ctr = True

