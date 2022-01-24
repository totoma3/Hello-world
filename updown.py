import random
computer=random.randint(1,100)
print(computer)
num=0

while True:
    user = int(input())
    if user<computer:
        num += 1
        print("업")
    elif user>computer:
        num += 1
        print("다운")
    elif user==computer:
        print("정답입니다.")
        print("시도 횟수는 %d번입니다."%num)
        break
