user_string = input("Write something, and I'll let you know the frequency of each word: ")
split_str = user_string.lower().split()

counting_dict = {}

for word in split_str:
    if word in counting_dict:
        counting_dict[word] += 1
    else:
        counting_dict[word] = 1

print(counting_dict)