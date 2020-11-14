import time, os
def header():
    os.system("cls");
    print(" ___ _     _____      _     _      ___  ")
    print("|_ _| |_  | ____|_  _(_)___| |_ __|__ \ ")
    print(" | || __| |  _| \ \/ / / __| __/ __|/ / ")
    print(" | || |_  | |___ >  <| \__ \ |_\__ \_|  ")
    print("|___|\__| |_____/_/\_\_|___/\__|___(_)  ")
    print("\n Lists must be generated with Database.py")
                                        
n=0
while n==0:
    header()
    print("\n1) Search Series\n")
    print("2) Search Movies")
    opt=str(input("\nEnter Option or (q)uit: "))
    try: 
        if opt =="1":
            header()
            series=input("\nEnter Series: ")
            with open ("C:/Users/User/Desktop/serieslist.txt",'r')as movies:
                for line in movies:
                    if series in line:
                        print("\nFound as: ",end="")
                        print(line)
                        input("\nPress Enter");break
                if series not in line:
                    print("\nNot Found");input("\nPress Enter")
        if opt =="2":
            header()
            movie=input("\nEnter Movie: ")
            with open ("C:/Users/User/Desktop/movielist.txt",'r')as movies:
                for line in movies:
                    if movie in line:
                        print("\nFound as: ",end="")
                        print(line)
                        input("\nPress Enter");break
                if movie not in line:
                    print("\nNot Found");input("\nPress Enter")
        if opt =="q":
            header()
            print("\nGoodbye");time.sleep(2)
            exit()
        else:
            header()
    except ValueError:
        header()
                    









