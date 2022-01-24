print("두 개의 양의 정수를 입력하세요:")
a=int(input())
b=int(input())
if a>b and a%2==0:
    print("%d 이 큰 수이고, 짝수이다."%a)
elif a<b and b%2==0:
    print("%d 이 큰 수이고, 짝수이다."%b)
elif a>b and a%2==1:
    print("%d 이 큰 수이고, 홀수이다." % a)
elif b>a and b%2==1:
    print("%d 이 큰 수이고, 홀수이다." % b)
