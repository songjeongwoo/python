from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):  # django.contrib.auth.forms 모듈의 UserCreationForm 클래스를 상속하고 email 속성을 추가
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")

# cf) UserCreationForm의 is_valid 함수는 계정생성 화면의 필드값 3개가 모두 입력되었는지, 비밀번호1과 비밀번호2가 같은지, 비밀번호의 값이 비밀번호 생성 규칙에 맞는지 등을 검사한다.