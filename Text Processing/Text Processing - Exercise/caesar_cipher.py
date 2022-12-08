text = input()
final_text = ''
for item in text:
    final_text += chr(ord(item) + 3)
print(final_text)
