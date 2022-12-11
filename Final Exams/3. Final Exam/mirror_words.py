import re

mirror_pairs = {}
text = input()
pattern = r"(#|@)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
word_pairs = re.findall(pattern, text)
if len(word_pairs) == 0:
    print("No word pairs found!")
else:
    print(f"{len(word_pairs)} word pairs found!")
for pairs in word_pairs:
    if pairs[1] == pairs[2][::-1]:
        word = pairs[1]
        mirror_pairs[word] = pairs[2]
if len(mirror_pairs) == 0:
    print("No mirror words!")
else:
    list_mirror_word = []
    print("The mirror words are:")
    for word, mirror in mirror_pairs.items():
        list_mirror_word.append(f'{word} <=> {mirror}')
    print(', '.join(list_mirror_word))
