try:
    user_input = float(input("Enter a number: "))
    print(f"Yay! {user_input} is a number")
except ValueError:
    print("Well, that is not a number, isn't it?")