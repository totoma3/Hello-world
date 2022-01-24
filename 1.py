T_shirt=10000
sweater=30000
T_num=int(input("티셔츠 개수 입력 : "))
s_num=int(input("스웨터 개수 입력 : "))
if T_num*T_shirt+sweater*s_num<=100000:
    print("합계 :  %d 원"%((T_num*T_shirt+sweater*s_num)*0.95))
elif T_num*T_shirt+sweater*s_num>100000:
    print("합계 :  %d 원"%((T_num*T_shirt+sweater*s_num)*0.85))
