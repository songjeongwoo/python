word = 'baekjoon'
alphabet = list(range(97,123))  # 아스키코드 숫자 범위(a~z는 97~122)

for x in alphabet :
    print(word.find(chr(x)), end= ' ')
'''
1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
'''

# chr()는 아스키코드에 해당하는 숫자를 문자열로 변환시키는 함수

'''
string.find(찾을 문자)
string.find(찾을 문자, 시작 idx)
string.find(찾을 문자, 시작 idx, 끝 idx)
시작 idx와 끝 idx는 생략하여 사용 가능

find()는 찾는 문자가 존재 한다면 해당 위치의 index를 반환해주고
찾는 문자가 존재 하지 않는다면 -1 을 반환
만약에 찾는 문자나 문자열이 여러개 있다면 맨 처음 찾은 문자의 index를 반환
'''