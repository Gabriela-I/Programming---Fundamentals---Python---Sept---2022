words = input().split()
palindrome = input()
list_with_palindromes = [word for word in words if word == word[::-1]]
print(list_with_palindromes)
count_palindromes = list_with_palindromes.count(palindrome)
print(f'Found palindrome {count_palindromes} times')