
# input :  한 줄의 문자열을 입력 받는 함수
# map : 입력받은 문자열을 특정한 자료형으로 변환 후 리스트화

n = int(input())
print(n)



data = list(map(int, input().split()))  # 공백을 기준으로 구분된 문자열을 리스트로 만듦.
data = input().split() # 원소의 갯수가 많지 않다면, 이렇게 간단히 사용해도 좋다.
print(data)
print(type(data))


# 반드시 저장되야하는 변수가 지정되어 있는 경우
a, b, c = map(int, input().split())

print(a, b, c)