def contains(this_key, substr):
    if substr in this_key:
        print(f"{key} contains {substr}")
    else:
        print("Substring not found!")
    return this_key


def flip(this_key, l_or_u, start, end):
    if l_or_u == 'Upper':
        new_substring = this_key[start:end].upper()
        this_key = this_key[:start] + new_substring + this_key[end:]
        print(this_key)
    else:
        new_substring = this_key[start:end].lower()
        this_key = this_key[:start] + new_substring + this_key[end:]
        print(this_key)
    return this_key


def slice_key(this_key, start, end):
    this_key = this_key[:start] + this_key[end:]
    print(this_key)
    return this_key


key = input()
while True:
    info = input().split('>>>')
    if info[0] == 'Generate':
        print(f"Your activation key is: {key}")
        break
    elif info[0] == 'Contains':
        substring = info[1]
        key = contains(key,substring)
    elif info[0] == 'Flip':
        u_or_l, start_index, end_index = info[1], int(info[2]), int(info[3])
        key = flip(key, u_or_l, start_index, end_index)
    else:
        start_index, end_index = int(info[1]), int(info[2])
        key = slice_key(key, start_index, end_index)