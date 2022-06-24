# 내장함수 : 파이썬이 기본적으로 제공하는 함수
# 사용자정의함수 : 개발자가 직접 정의하여 사용할 수 있는 함수

# 더하기 함수예제
from re import A


def add(a, b):
    return a + b

print(add(3,4))

# 더하기 함수예제 2
def add(a, b):
    print('함수의 결과: ', a + b)

add(4,5)

# global키워드
# global 키워드로 변수를 지정하면 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조하게 된다.
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)


# 여러개의 반환값을 가질 수 있다.
def operator(a,b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var
# packing : 여러 개의 반환값을 가지는 것

a, b, c, d = operator(7,3)
# unpacking : 여러 개의 반환값을 여러 개의 변수에 할당하는 것
print(a, b, c, d)



# 람다표현식
# 함수를 한 줄로 간단히 작성할 수 있다.

print((lambda a,b : a+b)(3,7))



# 여러 개의 리스트에 적용
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a, b : a + b, list1, list2)
print(list(result))