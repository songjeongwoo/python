'''
isalpha함수는 문자열이 문자인지 아닌지를 True,False로 리턴 
isdigit함수는 문자열이 숫자인지 아닌지를 True,False로 리턴
'''

num='111'
fake='hundred'
hanguel='한글'

#isdigit 사용
print(num.isdigit())  # True
print(fake.isdigit())  # False
print(hanguel.isdigit())  # False

#isalpha 사용
print(num.isalpha())  # False
print(fake.isalpha())  # True
print(hanguel.isalpha())  # True


# 출처: https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=lee95292&logNo=221201880034