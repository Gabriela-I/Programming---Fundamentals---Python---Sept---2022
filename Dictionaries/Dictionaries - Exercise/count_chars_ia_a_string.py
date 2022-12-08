word = input()
dictionary = {}
for letter in word:
    if letter.isalpha() and letter not in dictionary:
        dictionary[letter] = 0
    if letter.isalpha() and letter in dictionary:
        dictionary[letter] += 1
for key,value in dictionary.items():
    print(f"{key} -> {value}")