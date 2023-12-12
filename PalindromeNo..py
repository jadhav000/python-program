n=int(input('enter number : '))
sum=0

while n>0:
    z=n%10
    sum=(sum*10)+z
    n=n//10

if n==sum:
    print(f'{sum} is Palindrome Number ')
else:
    print(f'{sum} is not Palindrome Number ')