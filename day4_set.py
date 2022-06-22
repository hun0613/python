
# 중복을 제거
data = set([1,1,2,3,4,4,5])
print(data)


# 집합의 연산
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

# 합집합
print(a | b)

# 교집합
print(a & b)

# 차집합
print(a - b)



# 집합 관련 함수
data = set([1, 2, 3])
print(data)


# 새로운 원소 추가
data.add(4)
print(data)


# 새로운 원소 여러개 추가
data.update([5, 6])
print(data)


# 특정한 값을 갖는 원소 삭제
data.remove(5)
print(data)



"""
    리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있다.
    딕셔너리나 셋은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다.
        - 사전의 키(key) 혹은 집합의 원소를 이용해 O(1)의 시간복잡도로 조회.
"""
