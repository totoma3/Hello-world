a=input("비밀번호 입력: ")
if len(a)>=9:
    print("Your Password : Good")
elif len(a)>=5 and len(a)<9:
    print("Your Password : Normal")
elif len(a) <5:
    print("Your Password : Bad")
