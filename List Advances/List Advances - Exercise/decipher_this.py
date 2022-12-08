words = input().split()
final_list = []
for word in words:
    digits = []
    letters = []
    for letter in word:
        if letter.isdigit():
            digits.append(letter)
        else:
            letters.append(letter)
    if letters[0] in letters and letters[-1] in letters:
        letters[0], letters[-1] = letters[-1], letters[0]
    letters_as_string = ''.join(letters)
    number_as_string = ''.join(digits)
    deciphered_number = chr(int(number_as_string))
    final_word = str(deciphered_number) + letters_as_string
    final_list.append(final_word)
print(*final_list, sep=' ')
