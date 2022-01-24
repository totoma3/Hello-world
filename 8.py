import random
computer = random.choice(['가위', '바위', '보'])
user = int(input('하나를 선택하세요 : 가위(0), 바위(1), 보(2) : '))

if computer == '가위':
    print('컴퓨터는 가위를 냈습니다.')
    if user == 0:
        print('비겼습니다.')
    elif user == 1:
        print('당신이 이겼습니다.')
    elif user == 2:
        print('당신은 졌습니다.')
elif computer == '바위':
    print('컴퓨터는 바위를 냈습니다.')
    if user == 0:
        print('당신은 졌습니다.')
    elif user == 1:
        print('비겼습니다.')
    elif user == 2:
        print('당신이 이겼습니다.')
elif computer == '보':
    print('컴퓨터는 보를 냈습니다.')
    if user == 0:
        print('당신이 이겼습니다.')
    elif user == 1:
        print('당신은 졌습니다.')
    elif user == 2:
        print('비겼습니다.')
