# driver program
import Nov8


# function the uses an object as a parameter
def appinfo(obj, month, year):
    print(f"{obj} was created in {month} {year}")


# function that creates a list of objects
def makelist(n):  #n is the size of the list
    applist = []

    for i in range(n):
        name = input("App name: ")
        typ = input("App type: ")
        print()

        # creating object
        obj = Nov8.App(name, typ)

        # add to list
        applist.append(obj)

    return applist


def display(appl):
    for j in appl:
        print(j)


def main():
    tik = Nov8.App("TikTok", "Video Sharing")

    appinfo(tik, "September", 2016)

    size = int(input("Enter the number of apps you used today: "))

    apps = makelist(size)

    print("Here are the apps you used today: ")
    display(apps)


# ---call to main---
main()
