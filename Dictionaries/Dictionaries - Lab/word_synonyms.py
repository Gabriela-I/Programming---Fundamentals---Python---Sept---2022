number_of_the_keys = int(input())
synonyms = {}
for index in range(number_of_the_keys):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)
for key, value in synonyms.items():
    print(f"{key} - {', '.join(value)}")
