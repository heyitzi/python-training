def vowel_remover(str):
    for vowel in "aeiouAEIOU":
        str = str.replace(vowel, "*")
    return str

my_str = input("Write whatever you want, and I'll remove the vowels for you: ")
print(vowel_remover(my_str))

# TODO usar regex - library