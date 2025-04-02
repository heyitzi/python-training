def prime_num(num):
    if num > 1:
        for n in range(1, num):
            if num % n == 0:
                return f"{num} is not a prime number"
            else:
                return f"{num} is a prime number"
    else:
        return "I know, I know, 1 should be a prime number... but it's not!"

user_num = input("Enter a positive integer to find out if it's prime: ")
print(prime_num(int(user_num)))