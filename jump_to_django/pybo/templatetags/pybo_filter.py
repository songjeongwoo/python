from django import template

register = template.Library()


# 템플릿 필터 함수 만들기
@register.filter
def sub(value, arg):
    return value - arg
# cf) 더하기 필터(|add:5)를 사용한 것처럼 빼기 필터(|sub:3)가 있으면 좋겠지만 장고에는 빼기 필터가 없다.
# |add:-3처럼 하면 더하기 필터를 이용하여 원하는 값을 뺀 결과를 화면에 보여줄 수는 있다. 하지만 add 필터에는 변수를 적용할 수 없기 때문이다.