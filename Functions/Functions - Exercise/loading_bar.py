def loading_bar(num):
    if num == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    else:
        percent = '%' * (num//10)
        points = '.' * (10 - num//10)
        return f'{num}% [{percent}{points}]\nStill loading...'


number = int(input())
print(loading_bar(number))