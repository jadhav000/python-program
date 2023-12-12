n=5
for i in range(n):
    for j in range(n):
        if j==0 or j==4 or i==0 or i==2:
            print(j,end='')
        else:
            print(end=' ')
    print()



