try:
    f = open("29_demo.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("Sorry, the file you are trying to open doesn't exist.")