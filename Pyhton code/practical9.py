
from collections import Counter

def most_frequent_words(file_path):
    with open(file_path, 'r') as f:
        words = f.read().lower().split()
    return Counter(words).most_common(5)

# Test with your file
# print(most_frequent_words("example.txt"))
