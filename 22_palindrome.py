def palindrome(str):
    clean_str = ''.join(e for e in str if e.isalnum()).lower()
    if clean_str == clean_str[::-1]:
        return f"What kind of sorcery is this?! The word {str} is a palindrome"
    else:
        return f"{str} is such a boring word, it's not a palindrome..."

user_str = input("Do you want to know if a word is a palindrome? Write it here: ")
print(palindrome(user_str))

# TODO ignore spaces and symbols and capitalizations (convert to lower)