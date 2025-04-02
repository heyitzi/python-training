def palindrome(str):
    if str == str[::-1]:
        return f"What kind of sorcery is this?! The word {str} is a palindrome"
    else:
        return f"{str} is such a boring word, it's not a palindrome..."

user_str = input("Do you want to know if a word is a palindrome? Write it here: ")
print(palindrome(user_str))