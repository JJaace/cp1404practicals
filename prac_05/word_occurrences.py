"""
Word Occurrences
Estimate: 30 minutes
Actual: 40 minutes
"""
word_dictionary = {}
string = input("Enter string: ").lower()

words = string.split()

for word in words:
    word_dictionary[word] = word_dictionary.get(word, 0) + 1

sorted_words = sorted(word_dictionary.items())

for word, count in sorted_words:
    print(f"{word:15} : {count}")
