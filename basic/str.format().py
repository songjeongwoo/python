# 기본
just = "My name is {}, I'm {}".format("Hwang",36)
print(just)  # My name is Hwang, I'm 36

# 숫자 인덱스 사용(값이 많을 경우, 헷갈림 방지)
numbered = "My name is {0}, I'm {1}".format("Hwang",36)
print(numbered)  # My name is Hwang, I'm 36

# 변수 이름 사용(값이 많을 경우, 헷갈림 방지)
named = "My name is {fname}, I'm {age}".format(fname = "Hwang", age = 36)
print(named)  # My name is Hwang, I'm 36

# 출처: https://m.blog.naver.com/sw4r/221975908756