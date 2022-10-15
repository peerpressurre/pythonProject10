try:
    num1 = int(input('->'))
    num2 = int(input('->'))
    list = []
    counter = 0

    for i in range(num1,num2):
        counter = 0
        if i == 1:
            print(f'i, \t', end=' ')
            continue
        for j in range(1,num2+1):
            if i % j == 0:
               counter+=1
        if counter == 2:
            print(i, '\t', end=' ')
except Exception as ex:
    print(f'Error: {ex}')