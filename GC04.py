rows = 5 #number of rows for the pyramid

for i in range(rows):
    for j in range(rows-i):
        print(' ', end='') 
    for j in range(2*i+1):
        if j==0 or j==2*i or i==rows-1:
            print('A', end='')
        else:
            print(' ', end='')
    print()
