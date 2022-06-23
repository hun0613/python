#조건문

score = 85

if score >= 70:
    print('성적이 70점 이상입니다.')
elif score >= 60:
    print('성적이 60점 이상입니다.')
else:
    print('성적이 60점 미만입니다.')


# 논리 연산자
a = 15

if a <= 20 and a >= 0:
    print('Yes')


# 기타 연산자

score = 85

if score >= 80:
    pass # 나중에 작성할 코드
else:
    print("a < 80")


# 조건문의 간소화

if score >= 80: result = "Success"
else: result = "Fail"


score = 85
result = "Success" if score >= 80 else "Fail"

print(result)

