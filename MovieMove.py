import glob, os, shutil, sys, time

def header():
    os.system("cls")
    print("___  ___           _     ___  ___               ")
    print("|  \/  |          (_)    |  \/  |               ")
    print("| .  . | _____   ___  ___| .  . | _____   _____ ")
    print("| |\/| |/ _ \ \ / / |/ _ \ |\/| |/ _ \ \ / / _ \\")
    print("| |  | | (_) \ V /| |  __/ |  | | (_) \ V /  __/")
    print("\_|  |_/\___/ \_/ |_|\___\_|  |_/\___/ \_/ \___|")
    print("\nUse this for movies (i.e. Movie.mp4), not series (i.e. [S01E01]Series.mp4).\n")

header()

p=input("Enter Path (i.e D:/Media/TV/): ")
f=input("\n\nEnter File Type (i.e. mp4): ")
path=p+"*."+f
fullpaths=[];movie_names=[]
for dirs in glob.glob(path):
    movie_names.append(str(dirs).split("\\")[1].split(".mp4")[0])
    fullpaths.append(dirs) #source
if len(fullpaths) < 1:
    header()
    print("No movie files found. Ending.");time.sleep(2)
    exit()
newpath="D:/Media/Movies/"
n=0;directories=[]
while n <len(movie_names):
    makedirs=newpath+str(movie_names[n])
    os.mkdir(makedirs)
    directories.append(makedirs) #dest
    n=n+1
header()
print("These movies: \n");print(*movie_names,sep="\n")
print("\nWill move from: '"+str(fullpaths[0]).split("\\")[0]+"/' To: '"+newpath)
yn=input("\nCorrect (y/n): ")
while True:
    try:
        if yn == "y":
            c=0;
            while c<len(fullpaths):
                shutil.move(fullpaths[c],directories[c])
                c=c+1
        if yn == "n":
            break
        print("\nDone...\n\nExiting...");time.sleep(2)
        exit()
    except ValueError:
        header()
        yn=input("Correct (y/n): ")


