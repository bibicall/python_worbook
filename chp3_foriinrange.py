limit = int(input("Enter an integer: "))

print('The multiples of 3 up to and including ' +str(limit)+ ' are: ')
for i in range(3, limit+1, 3):
    print(i)