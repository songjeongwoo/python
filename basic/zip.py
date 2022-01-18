numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for pair in zip(numbers, letters):
    print(pair)

'''
(1, 'A')
(2, 'B')
(3, 'C')
'''

for number, upper, lower in zip("12345", "ABCDE", "abcde"):
    print(number, upper, lower)

'''
1 A a
2 B b
3 C c
4 D d
5 E e
'''
# 출처: https://www.daleseo.com/python-zip/