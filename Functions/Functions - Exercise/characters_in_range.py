def collect_characters(first, second):
    list_with_character = []
    for element in range(ord(first)+1, ord(second)):
        list_with_character.append(chr(element))
    return list_with_character


character_one = input()
character_two = input()
result = collect_characters(character_one, character_two)
print(*result, sep=' ')