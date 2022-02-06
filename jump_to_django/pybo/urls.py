from django.urls import path

from . import views

# URL 별칭 사용 시 중복을 피하기 위해 URL namespace를 설정
app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]