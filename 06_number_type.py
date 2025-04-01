def num_type(number):
    if number < 0:
        return f"{number} is negative"
    elif number > 0:
        return f"{number} is positive"
    else:
        return f"{number} is zero"

user_num = input("Enter your number: ")

print(num_type(int(user_num)))