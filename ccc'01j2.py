def modinverse():
    a = int(input())
    b = int(input())
    for i in range(1, b, 1):
        if (a * i) % b == 1:
            print(i)
            break
        elif i == b - 1 and (a * i) % b != 1:
            print('No such integer exists.')

modinverse()