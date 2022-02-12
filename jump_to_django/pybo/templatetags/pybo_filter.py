import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


# 템플릿 필터 함수 만들기
@register.filter
def sub(value, arg):
    return value - arg
# cf) 더하기 필터(|add:5)를 사용한 것처럼 빼기 필터(|sub:3)가 있으면 좋겠지만 장고에는 빼기 필터가 없다.
# |add:-3처럼 하면 더하기 필터를 이용하여 원하는 값을 뺀 결과를 화면에 보여줄 수는 있다. 하지만 add 필터에는 변수를 적용할 수 없기 때문이다.


@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))
'''
mark 함수는 markdown 모듈과 mark_safe 함수를 이용하여 입력 문자열을 HTML로 변환하는 필터 함수이다.
마크다운에는 몇 가지 확장 기능이 있는데 파이보는 위처럼 nl2br과 fenced_code를 사용하도록 설정했다.
nl2br은 줄바꿈 문자를 <br> 로 바꾸어 준다.
fenced_code는 위에서 살펴본 마크다운의 소스코드 표현을 위해 필요하다.

cf) 마크다운 확장 기능 문서: https://python-markdown.github.io/extensions/
'''
