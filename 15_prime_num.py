def prime_num(num):
    if num == 2:
        return f"{num} is a prime number"
    elif num > 2:
        for n in range(2, num):
            if num % n == 0:
                return f"{num} is not a prime number"
        return f"{num} is a prime number"
    elif num <= 0:
        return "Only positive numbers can be prime, please enter a valid option."
    else:
        return "I know, I know, 1 should be a prime number... but it's not!"

user_num = input("Enter a positive integer to find out if it's prime: ")
print(prime_num(int(user_num)))