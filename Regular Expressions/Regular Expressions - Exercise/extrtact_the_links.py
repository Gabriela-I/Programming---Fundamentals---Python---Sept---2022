import re

text = input()
while text:
    pattern = r'www\.[A-Za-z0-9\-]+\.[a-z]+[.a-z]*'
    emails = re.findall(pattern, text)
    if emails:
        print(''.join(emails))
    text = input()