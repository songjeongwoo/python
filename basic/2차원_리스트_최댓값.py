# 다음 2차원 리스트인 a에서 최댓값을 구하라.
a = [ [0, 9, 9], [1, 2, 3] ]

print(max(max(a)))  # 3 - 오답
'''
풀이과정:
max(a) = [1, 2, 3]
max(max(a)) = 3
'''

print(max(max(row) for row in a))  # 9 - 정답
'''
풀이과정:
[row for row in a] = [ [0, 9, 9], [1, 2, 3] ]
[max(row) for row in a] = [9, 3]
따라서,
max(max(row) for row in a) = 9
'''