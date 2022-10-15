try:
   num1 = int(input('->'))
   num2 = int(input('->'))

   for i in range(num1, num2):
       for j in range(num1, num2):
           print(f'{i} * {j} =', i * j, end="\t")
       print("\n")
except Exception as ex:
    print(f'Error: {ex}')