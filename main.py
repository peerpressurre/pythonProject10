try:
    num1 = int(input('->'))
    num2 = int(input('->'))
    list = []
    for i in range(num1,num2):
        for j in range(num1,num2):
            if i % i == 0 and i % j != 0:
               list.append(i)

    print(f'{list}')
except Exception as ex:
    print(f'Error: {ex}'