import re

text = input()
threshold = 1
for symbols in text:
    if symbols.isdigit():
        threshold *= int(symbols)
pattern = r'(::|\*\*)([A-Z][a-z]{2,})\1'
match = re.findall(pattern, text)
print(f'Cool threshold: {threshold}')
print(f"{len(match)} emojis found in the text. The cool ones are:")
for emoji in match:
    ascii_emoji = [ord(character) for character in emoji[1]]
    if sum(ascii_emoji) > threshold:
        print(emoji[0] + emoji[1] + emoji[0])
