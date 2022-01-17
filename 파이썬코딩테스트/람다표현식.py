# 람다표현식 : 이름없는 함수
# 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 장점
def add(a, b):
    return a + b


print(add(3, 7))

print((lambda a, b: a + b)(3, 7))

# sorted() 함수에서 람다함수를 속성의 값으로 사용할 수 있다.
array = [('홍길동', 50), ('이순신', 532), ('아무개', 72)]


def my_key(x):
    return x[1]


print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# 람다표현식 여러개의 리스트에 동일한 규칙을 가지는 하나의 함수를 적용하고자 할때
# map함수 : 각각의 원소에 어떠한 함수를 적용 하고자 할때 사용할 수 있다.
result = map(lambda a, b: a + b, list1, list2)

print(list(result))  # 결과[7, 9, 11, 13, 15]
