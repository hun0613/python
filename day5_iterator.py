#반복문


i = 1
result = 0

while i <= 9:
    result += i
    i += 1


print(result)


# 홀수의 합
while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1


print(result)



# for문

array = [9, 8, 7, 6, 5]

for x in array:
    print(x)


result = 0
for i in range(1,10):
    result += i

print(result)



# continue

for i in range(1,10):
    if i % 2 == 0:
        continue
    result += i

print(result)



# break

i = 1

while True:
    print("현재 i의 값:", i)
    if i == 5:
        break
    i += 1


# 학생들의 합격 여부 판단 예제
# 점수가 80점만 넘으면 합격

"""
학생점수 리스트 생성
while문을 활영해 리스트 안의 원소를 훑기
    - 만약 점수가 80점 이상이면
        - "[인덱스값]번 학생은 합격입니다" 출력

"""


score = [30, 60, 90, 85, 99]
i = 0



while i < len(score):
    if score[i] >= 80:
        print(f'{i+1}번째 학생은 합격입니다.')
    
    i += 1



"""
학생점수 리스트 생성
while문을 활영해 리스트 안의 원소를 훑기
    - 만약 점수가 80점 이상이면
        - "[인덱스값]번 학생은 합격입니다" 출력

"""
# 기능추가 : 2,4번 학생은 부정행위 학생이므로 제외하고 출력할 것

score = [30, 60, 90, 85, 99]
cheating_student = (2, 4)

i = 0

for i in range(len(score)):
    if i + 1 in cheating_student:
        continue
    if score[i] >= 80:
        print(f'{i+1}번째 학생은 합격입니다.')