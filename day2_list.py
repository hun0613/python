

# 배열
a = [1,2,3,4,5,6,7,8,9]
print(a)


# 배열의 인덱싱
print(a[3])
print(a[-1]) #뒤에 첫번째 원소 출력


# 배열 생성 후, 해당 속성을 n번 반복
n = 10
a = [0] * n
print(a)


# 배열의 슬라이싱
# 끝 인덱스는 실제 인덱스보다 1이 크다.
a = [1,2,3,4,5,6,7,8,9]
print(a[1:4])


# 리스트 컴프리헨션
array = [i for i in range(10)] # 반복문의 i의 값이 순서대로 array의 원소로 삽입된다.
print(array)

array2 = [i for i in range(10) if i % 2 == 1]
print(array2)

array3 = [i * i for i in range(10)]
print(array3)



# 언더바
for _ in range(5):
    print('helloworld')


# append
a = ['a','b','c','d','e']
a.append('f')
print(a)


# sort
a = ['b','a','f','e','d'] 
a.sort() #오름차순
print(a)

a.sort(reverse=True)  #내림차순
print(a)

# reverse
a = ['b','a','f','e','d'] 
a.reverse()
print(a)


#insert
a = ['b','a','f','e','d'] 
a.insert(0,'z')
print(a)



#remove
a = ['b','a','f','e','d'] 
a.remove('f')
print(a)