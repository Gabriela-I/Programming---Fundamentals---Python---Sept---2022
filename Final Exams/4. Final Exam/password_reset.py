def cut(pas, index, length):
    pas = pas[:index] + pas[index + length:]
    print(pas)
    return pas


def take_odd(pas):
    new_pass = ''
    for index in range(1, len(pas), 2):
        new_pass += pas[index]
    pas = new_pass
    print(pas)
    return pas


def substitute(pas, part, replacement_text):
    if part in pas:
        while part in pas:
            pas = pas.replace(part, replacement_text)
        print(pas)
    else:
        print('Nothing to replace!')

    return pas


def password_func(pas):
    while True:
        info = input().split()
        command = info[0]
        if command == 'Done':
            print(f"Your password is: {pas}")
            break
        elif command == 'TakeOdd':
            pas = take_odd(pas)
        elif command == 'Cut':
            index, length = int(info[1]), int(info[2])
            pas = cut(pas, index, length)
        else:
            part, replacement_text = info[1], info[2]
            pas = substitute(pas, part, replacement_text)


password = input()
password_func(password)
