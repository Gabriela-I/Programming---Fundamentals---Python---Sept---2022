capacity_of_tank = 255
number_of_lines = int(input())
counter_of_liters = 0
for number in range(number_of_lines):
    current_line = int(input())
    counter_of_liters += current_line
    if counter_of_liters > capacity_of_tank:
        print("Insufficient capacity!")
        counter_of_liters -= current_line
        continue
print(counter_of_liters)
