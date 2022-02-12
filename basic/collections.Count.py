'''
1.list.count(x): 배열 내 주어진 원소 x의 개수를 셈(문자열 가능).
2.collections의 Counter(iterable): 배열, 문자열, 딕셔너리 내 모든 원소의 개수 셈.
'''

# 1. list.count(x)
array = ['a', 'b', 'c', 'ae', 'ba', 'dab']
cnt = array.count('a')
print('배열 내 a의 등장 횟수 :', cnt)  # > 배열 a의 등장 횟수 : 1

# 2. collections의 Counter(iterable)
from collections import Counter

cnt = Counter(['a', 'b', 'c', 'ae', 'ba', 'dab'])
print('배열 내 각 원소를 세는 카운터 :', cnt)
# > 배열 내 각 원소의 갯수 : Counter({'a': 1, 'b': 1, 'c': 1, 'ae': 1, 'ba': 1, 'dab': 1})

cnt = Counter('Abracadabra!')
print('문자열 내 각 원소를 세는 카운터 :', cnt)
# 문자열 내 각 원소를 세는 카운터 : Counter({'a': 4, 'b': 2, 'r': 2, 'A': 1, 'c': 1, 'd': 1, '!': 1})


# 출처: https://dev-note-97.tistory.com/17


## 응용(백준 1157번)
from collections import Counter
s = input()
s = s.upper()
s = sorted(s)
cnt = Counter(s)
if len(s) == 1:
    print(s[0])
else:
    tmp = cnt.most_common(2)
    if tmp[0][1] == tmp[1][1]:
        print('?')
    else:
        print(tmp[0][0])