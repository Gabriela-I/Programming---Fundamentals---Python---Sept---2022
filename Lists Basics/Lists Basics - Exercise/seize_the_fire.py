fire_with_cells = input().split('#')
water = int(input())
effort = 0
cells_put_out = []
for fire in fire_with_cells:
    type_of_fire = fire.split(' = ')[0]
    value_of_cell = int(fire.split(' = ')[1])
    if value_of_cell <= water:
        if type_of_fire == 'High' and 81 <= value_of_cell <= 125 or \
                type_of_fire == 'Medium' and 51 <= value_of_cell <= 80 or \
                type_of_fire == 'Low' and 1 <= value_of_cell <= 50:
            water -= value_of_cell
            effort += value_of_cell * 0.25
            cells_put_out.append(value_of_cell)
total_fire = sum(cells_put_out)
print('Cells:')
for cell in cells_put_out:
    print(f' - {cell}')
print(f'Effort: {effort:.2f}')
print(f"Total Fire: {total_fire}")