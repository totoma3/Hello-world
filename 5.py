n=int(input("1 이상의 정수 입력: "))
print("%d 의 약수"%n)
lst=[]
for i in range(1,n+1):
    if n%i==0:
        lst.append(i)
for j in lst:
    print(j)
