print("SIGN IN")
print("----------")

username_list = []
password_list = []

while True:
    print("----------")
    print("OPTIONS")
    print("-----")
    print("1. Log in to your account")
    print("2. Create a new account")
    print("3. Leave program")
    print("----------")

    option = int(input("Enter an option (1/2/3): "))

    if option == 1:
        print("----------")
        print("Log in:")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username_list.index(username) != -1 and password_list.index(password) != -1:
            print("----------")
            print("Welcome! You have successfully logged in")
            print("----------")
        else:
            print("----------")
            print("Sorry, the username or password you have entered is incorrect")
            print("Please try again")
            print("----------")
    elif option == 2:
        print("Create a new account:")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username_list.index(username) != -1:
            print("----------")
            print("Sorry, the username already exists")
            print("Please try again")
            print("----------")
        else:
            print("----------")
            print("Yay! You have successfully created your account")
            print("You can now log in")
            print("----------")
    elif option == 3:
        break
    else:
        print("Sorry, enter a valid option")