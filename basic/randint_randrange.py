from random import randint, randrange

# randint(a, b) - a이상 b이하의 랜덤한 정수
res = set()
for _ in range(10000):
    # 1부터 100 사이의 랜덤한 정수
    res.add(randint(1, 5))

print(res)  # {1, 2, 3, 4, 5}

# randrange(a, b) - a이상 b미만의 랜덤한 정수
# cf) randrange(a, b, step)
res = set()
for _ in range(10000):
    # 1부터 100 사이의 랜덤한 정수
    res.add(randrange(1, 5))

print(res)  # {1, 2, 3, 4}

# randrange(a, b, step) - a이상 b미만의 범위에서, step만큼 뛰면서 랜덤한 정수
res = set()
for _ in range(10000):
    # 1부터 100 사이의 랜덤한 정수
    res.add(randrange(1, 5, 2))

print(res)  # {1, 3}


# 출처: https://codingdog.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-randint-randrange-%EB%9E%9C%EB%8D%A4%ED%95%98%EA%B2%8C-%EC%88%98%EB%A5%BC-%EB%BD%91%EC%9D%84-%EB%95%8C-%EC%93%B4%EB%8B%A4