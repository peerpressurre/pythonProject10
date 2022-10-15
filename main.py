try:
   num1 = int(input('->'))
   num2 = int(input('->'))

   for i in range(1,10):
       for j in range(num1, num2+1):
           print(f'{j} * {i} =', i * j, end="\t\t")
       print("")
except Exception as ex:
    print(f'Error: {ex}')