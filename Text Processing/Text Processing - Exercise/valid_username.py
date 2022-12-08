def length_is_valid(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def characters_is_valid(username):
    for letter in username:
        if not (letter.isalnum() or letter == '_' or letter == '-'):
            return False
    return True


def no_redundant_symbols(username):
    if ' ' in username:
        return False
    return True


def username_is_valid(username):
    if length_is_valid(username) and characters_is_valid(username) and no_redundant_symbols(username):
        return True
    return False


usernames = input().split(', ')
for name in usernames:
    if username_is_valid(name):
        print(name)
