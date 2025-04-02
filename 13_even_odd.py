def even_odd(num):
    if num % 2 == 0:
        return f"{num} is an even number!"
    else:
        return f"{num} is an odd number!"
    
user_num = input("Enter a number to find out if it's even or odd: ")
print(even_odd(int(user_num)))