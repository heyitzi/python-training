import random
import nltk
from nltk.corpus import brown
import os

# Ensure the Brown corpus is downloaded
nltk.download('brown')

# Get a large pool of English words from the Brown corpus
words_pool = brown.words()

# Create a 10,000-word list by sampling with replacement
sampled_words = random.choices(words_pool, k=10000)

# Join words into a single string
text_content = ' '.join(sampled_words)

# Save to a text file
file_path = './word_count_exercise.txt'
with open(file_path, 'w') as file:
    file.write(text_content)

file_path
