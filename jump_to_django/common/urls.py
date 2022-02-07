from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),  # 로그인 뷰는 따로 만들 필요없이 django.contrib.auth 앱(기본 앱)의 LoginView를 사용한다.
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]

'''
cf) LoginView는 registration이라는 템플릿 디렉터리에서 login.html 파일을 찾는다.
    즉, registration/login.html 템플릿 파일을 작성해야 한다.
    
    다만! 로그인은 common 앱에 구현할 것이므로 오류 메시지에 표시한 것처럼 registration 디렉터리에 템플릿 파일을 생성하기보다는 common 디렉터리에 템플릿을 생성하는 것이 좋다.
    이를 위해 LoginView가 common 디렉터리의 템플릿을 참조할 수 있도록
    auth_views.LoginView.as_view()를
    auth_views.LoginView.as_view(template_name='common/login.html')로 수정한다.
'''