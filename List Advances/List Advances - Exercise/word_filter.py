words = input().split()
filtered = [word for word in words if len(word) % 2 == 0]
print('\n'.join(filtered))




# words = input().split()
# filtered = list(filter(lambda x: len(x) % 2 == 0, words))
# [print(word) for word in filtered]
