start_char = int(input())
finish_char = int(input())
for char in range(start_char, finish_char + 1):
    current_char = chr(char)
    print(current_char, end=' ')