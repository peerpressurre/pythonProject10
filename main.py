try:
   for i in range(1, 10):
       for j in range(1, 10):
           print(f'{i} * {j} =', i * j, end="\t")
       print("\n")
except Exception as ex:
    print(f'Error: {ex}'