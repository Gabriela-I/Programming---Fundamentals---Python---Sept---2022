numbers = input().split()
abs_number = []
for element in numbers:
    abs_number.append(abs(float(element)))
print(abs_number)