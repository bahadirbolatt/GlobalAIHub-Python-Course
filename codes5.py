def multpl(*args):
    result = 1
    for number in args:
        result *= number
    print(result)

multpl(9, 3, 0 ,4)