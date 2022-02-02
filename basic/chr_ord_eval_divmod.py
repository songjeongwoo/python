'''
chr(i)는 유니코드(Unicode) 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수이다.
※ 유니코드는 전 세계의 모든 문자를 컴퓨터에서 일관되게 표현하고 다룰 수 있도록 설계된 산업 표준이다.
'''

chr(97)
# 'a'
chr(44032)
# '가'

'''
ord(c)는 문자의 유니코드 값을 돌려주는 함수이다.
※ ord 함수는 chr 함수와 반대이다.
'''

ord('a')
# 97
ord('가')
# 44032

'''
eval(expression)은 실행 가능한 문자열(1+2, 'hi' + 'a' 같은 것)을 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수이다.
'''
eval('1+2')
# 3
eval("'hi' + 'a'")
# 'hia'
eval('divmod(4, 3)')
# (1, 1)

'''
divmod(a, b)는 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수이다.
'''
divmod(7, 3)
# (2, 1)

'''
cf) 몫을 구하는 연산자 //와 나머지를 구하는 연산자 %를 각각 사용한 결과와 비교해 보자.
'''

7 // 3
# 2
7 % 3
# 1