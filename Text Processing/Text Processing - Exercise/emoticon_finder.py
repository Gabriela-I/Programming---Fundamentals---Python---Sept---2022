text = input()
for character in range(len(text)):
    if text[character] == ':':
        print(':' + text[character + 1])