def turntables(num, type):
    if type == 1:
        return num
    else:
        return str(num)


user_num = input("Enter a number of your choice: ")
user_type = input("Choose 1 if you want to return it as a number or 2 if you prefer a string")

print(turntables(int(user_num), int(user_type)))