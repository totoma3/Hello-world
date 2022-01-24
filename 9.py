while True:
    a=int(input("가고자 하는 층 입력: "))
    b=int(input("현재 위치 입력: "))
    if a<1 or a>7:
        print("1~6층 버튼만 눌러주세요.")
        pass
    elif a==b:
        print("다른 층(1~6)을 눌러주세요.")
        pass
    elif b>a:
        for i in range(b,a-1,-1):
            print("현재 층은 %d 입니다."%i)
        print("%d 층에 도착하였습니다. 안녕히 가세요."%a)
        break
    elif b<a:
        for i in range(b,a+1):
            print("현재 층은 %d 입니다."%i)
        print("%d 층에 도착하였습니다. 안녕히 가세요"%a)
        break
