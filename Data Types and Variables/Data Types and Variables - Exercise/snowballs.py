number_of_balls = int(input())
best_value = 0
best_weight = 0
best_time = 0
best_quality = 0
for ball in range(number_of_balls):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight / time) ** quality
    if value > best_value:
        best_value = value
        best_time = time
        best_weight = weight
        best_quality = quality
print(f"{best_weight} : {best_time} = {int(best_value)} ({best_quality})")