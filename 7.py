contractPrice=int(input("계약 금액 입력: "))
period=int(input("사용 개월 수 입력: "))
cardCode=int(input("카드 코드 입력: "))
if period<=6:
    if cardCode==11:
        print("최종 요금은 %d 원입니다."%(contractPrice*0.95))
    elif cardCode==12:
        print("최종 요금은 %d 원입니다." % (contractPrice *0.92))
    elif cardCode==13:
        print("최종 요금은 %d 원입니다." % (contractPrice * 0.88))
elif period>6 and period<=12:
    if cardCode == 11:
        print("최종 요금은 %d 원입니다." % (contractPrice * 0.90*0.95))
    elif cardCode == 12:
        print("최종 요금은 %d 원입니다." % (contractPrice * 0.90*0.92))
    elif cardCode == 13:
        print("최종 요금은 %d 원입니다." %(contractPrice * 0.90*0.88))
elif period>12:
    if cardCode == 11:
        print("최종 요금은 %d 원입니다." % (contractPrice * 0.80*0.95))
    elif cardCode == 12:
        print("최종 요금은 %d 원입니다." % (contractPrice * 0.80*0.92))
    elif cardCode == 13:
        print("최종 요금은 %d 원입니다." % (contractPrice * 0.80*0.88))
