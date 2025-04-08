#  Diary App: Save entries to a file with timestamps

import datetime

f = open("01_my_diary.txt", "a")

date = datetime.datetime.now()
user_diary = input("Enter your new diary entry: ")

f.write(date.strftime("%Y-%m-%d %H:%M:%S") + "\n" + user_diary + "\n\n")
f.close()

f = open("01_my_diary.txt", "r")
print("-----")
print(f.read())