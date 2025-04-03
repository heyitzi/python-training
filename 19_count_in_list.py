my_list = ["a", "b", "c", "a", "a", "a", "c", "b", "d", "e", "d", "c"]

# my_dict = {letter: my_list.count(letter) for letter in my_list}
# print(my_dict)

# TODO hacer de manera normal

new_dict = {}

for letter in my_list:
    if letter in new_dict:
        new_dict[letter] += 1
    else:
        new_dict[letter] = 1

print(new_dict)