a=12345
n=0
while(a>0):
    g=a%10
    p=g**g
    
    n=n+p


    a=a//10
print(n)