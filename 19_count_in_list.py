my_list = ["a", "b", "c", "a", "a", "a", "c", "b", "d", "e", "d", "c"]

my_dict = {letter: my_list.count(letter) for letter in my_list}

print(my_dict)