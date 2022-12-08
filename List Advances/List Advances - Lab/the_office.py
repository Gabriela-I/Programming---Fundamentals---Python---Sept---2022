employees_happiness = list(map(int, input().split()))
factor = int(input())
happiness_check = [person * factor for person in employees_happiness]
average = sum(happiness_check) / len(employees_happiness)
half_employees = len(employees_happiness) // 2
filtered_list = list(filter(lambda x: x >= average, happiness_check))
if len(filtered_list) >= half_employees:
    print(f'Score: {len(filtered_list)}/{len(employees_happiness)}. Employees are happy!')
else:
    print(f"Score: {len(filtered_list)}/{len(employees_happiness)}. Employees are not happy!")


# def filtered_employees(check, value_of_average):
#     count = 0
#     for employee in check:
#         if employee >= value_of_average:
#             count += 1
#     return count
#
#
# employees_happiness = list(map(int, input().split()))
# factor = int(input())
# happiness_check = [person * factor for person in employees_happiness]
# average = sum(happiness_check) / len(employees_happiness)
# half_employees = len(employees_happiness) // 2
# count_of_persons = filtered_employees(happiness_check, average)
# if count_of_persons >= half_employees:
#     print(f'Score: {count_of_persons}/{len(employees_happiness)}. Employees are happy!')
# else:
#     print(f"Score: {count_of_persons}/{len(employees_happiness)}. Employees are not happy!")