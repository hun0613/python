from re import A


data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("'사과'가 data에 있습니다.")



# 메서드

# 키 데이터만 담은 리스트
key_list = data.keys()

# 값 데이터만 담은 리스트
value_list = data.values()

print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])