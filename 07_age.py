def age_controller(age):
    if age <= 18:
        return "Oh no, you are not 18 so you cannot drive or drink. Don't worry, soon enough you will wish to return to your current age."
    else:
        return "Yay! You can drive and drink. How's that existential dread going?"

user_age = input("How old are you?: ")
print (age_controller(int(user_age)))