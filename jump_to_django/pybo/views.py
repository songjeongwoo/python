from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request):
    '''
    pybo 목록 출력
    '''
    question_list = Question.objects.order_by('-create_date')  # 내림차순 정렬
    context = {'question_list': question_list}

    # render 함수는 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수
    # cf) 템플릿 파일은 HTML 파일과 비슷하지만 장고에서 사용하는 태그를 사용할수 있는 HTML 파일이다.
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    '''
    pybo 내용 출력
    '''
    # question = Question.objects.get(id=question_id) 이 경우, 없는 id로 접속하면 DoesNotExist 에러
    question = get_object_or_404(Question, pk=question_id)  # 에러가 Page not found(404)로 바뀜
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


# 제네릭 뷰는 추후에