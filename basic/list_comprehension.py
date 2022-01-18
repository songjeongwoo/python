li=[]
for i in range(5):
    li.append(i)

# List Comprehension 적용
li = [i for i in range(5)]

# 응용1 - 수식 또는 함수 적용가능
def test(x):
    x = str(x) + 'ab'
    return x
 
[test(i) for i in range(5)]
'''
# 출력 결과
['0ab', '1ab', '2ab', '3ab', '4ab']
'''

# 응용2 - 오른쪽에 if문 사용
[i for i in range(5) if i % 2 == 0]
'''
# 출력 결과
[0, 2, 4]
'''

# 응용3 - 오른쪽에 if문 여러 개 사용
[i for i in range(5) if i % 2 == 0 if i % 4==0]
'''
# 출력 결과
[0, 4]

# 코드 설명
if i%2==0과 if i%4==0은 and 조건으로 묶여 동시에 만족하는 경우만 출력
'''

# 응용4 - 왼쪽에 if문 사용(반드시 else와 같이 사용)
[i if i % 2 == 0 else 'odd' for i in range(5)]
'''
# 출력 결과
[0, 'odd', 2, 'odd', 4]
'''

# 응용5 - 왼쪽에 if문 여러 개 사용(반드시 else와 같이 사용)
[i if i%2 == 0 else 'odd-1' if i == 1 else 'odd-3'  for i in range(5)]
'''
# 출력 결과
[0, 'odd-1', 2, 'odd-3', 4]

# 코드 설명
i if i%2==0 : i가 2로 나누어 떨어지면 i를 그대로 출력
else 'odd-1' if i==1: 2로 나누어 떨어지지 않으면, i가 1일 때 'odd-1' 출력★★
else 'odd-3' : 위의 두 조건이 모두 성립하지 않으면 'odd-3' 출력
'''
# 출처: https://bio-info.tistory.com/28