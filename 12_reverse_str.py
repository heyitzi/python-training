word = input("Write and I'll reverse it: ")

print(word[::-1])

# TODO explore slice more

# string[start_position:end_position:step]
# start_position (included) / end position (excluded)

s = "My name is Itz"
s1 = s[3:12:3]
print(s1)

s2 = "AnotherString"
s3 = s2[:1:-1]
print(s3)