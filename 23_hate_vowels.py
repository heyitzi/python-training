# def vowel_remover(str):
#     for vowel in "aeiouAEIOU":
#         str = str.replace(vowel, "*")
#     return str

import re

my_str = input("Write whatever you want, and I'll remove the vowels for you: ")
# print(vowel_remover(my_str))

hate_vowels = re.sub("[aeiouAEIOU]", "*", my_str)
print(hate_vowels)