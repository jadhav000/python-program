n=int(input('enter number : '))
sum=0

while n>0:
    z=n%10
    sum=sum+(z**3)
    n=n//10

print(sum)

