f = open("29_demo.txt", "a")

user_text = input("Enter what you want to add to the text file: ")

f.write(user_text +  "\n")
f.close()

f = open("29_demo.txt", "r")
print(f.read())

# a - append
# w - write (overwrite)
# x - create file