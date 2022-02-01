# sort()
# - 리스트 자료형에서만 사용 가능하다.
# - 원래의 리스트가 변경된다(in-place).
# - 리스트를 정렬할 땐 sorted()보다 빠르다.
list.sort()

# 내림차순
list.sort(reverse=True)

# sorted()
# - 모든 iterable한 객체에서 사용 가능하다.
# - 정렬된 새로운 리스트를 반환한다.
sorted(iterable)
sorted(iterable, key=function)
sorted(iterable, key=function, reverse=True)

# ex)
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

print(sorted(array, key=lambda x: x[1]))
'''
[('이순신', 32), ('홍길동', 50), ('아무개', 74)]
'''
# 내림차순
print(sorted(array, key=lambda x: -x[1]))
'''
[('아무개', 74), ('홍길동', 50), ('이순신', 32)]
'''