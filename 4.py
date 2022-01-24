a,b,c=list(map(int,input().split()))
if (a+b+c)%2==0:
    print(max(a,b,c))
elif (a+b+c)%2==1:
    print(a+b+c)
