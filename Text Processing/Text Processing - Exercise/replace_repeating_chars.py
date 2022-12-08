text = input()
result = ''
for character in range(len(text)):
    if character + 1 < len(text):
        if text[character] != text[character + 1]:
            result += text[character]
    else:
        result += text[character]
print(result)