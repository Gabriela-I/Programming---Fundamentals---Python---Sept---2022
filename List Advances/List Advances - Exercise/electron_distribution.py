number_of_electrons = int(input())
filled_shells = []
position_of_shell = 1
while number_of_electrons > 0:
    max_electrons = 2 * (position_of_shell ** 2)
    if max_electrons <= number_of_electrons:
        filled_shells.append(max_electrons)
        position_of_shell += 1
        number_of_electrons -= max_electrons
    elif max_electrons > number_of_electrons:
        filled_shells.append(number_of_electrons)
        number_of_electrons -= number_of_electrons
print(filled_shells)


