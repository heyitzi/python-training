# Word Counter: Read a file and report most common words

file_path = 'word_count_exercise.txt'

f = open(file_path, "r")
text = f.read()

split_txt = text.lower().split()

counting_dict = {}

for word in split_txt:
    if word in counting_dict:
        counting_dict[word] += 1
    else:
        counting_dict[word] = 1

max_value = max(counting_dict.values())
max_key = [key for key, value in counting_dict.items() if value == max_value]

most_used_word = max_key[0]

print(f"The word \"{most_used_word}\" is the most popular one, used {max_value} times.")