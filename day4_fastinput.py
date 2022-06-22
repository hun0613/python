# 사용자로부터 빠르게 입력을 받아와야될 경우

import sys

#문자열 입력받기
data = sys.stdin.readline().rstrip() #sys.stdin.readline() -> input보다 빠르게 입력을 받아옴 / 엔터기호가 자동으로 삽입되기 때문에 rsstrip()함수를 이용하여 제거.
print(data)



# 출력을 위한 전형적인 소스코드
a = 1
b = 2
print(a, b)


# 줄바꿈 안함
print(7, end=" ")
print(8, end=" ")

answer = 7
print("정답은" + str(answer) + "입니다.")


# f-string
answer = 10
print(f"정답은 {answer} 입니다.")


