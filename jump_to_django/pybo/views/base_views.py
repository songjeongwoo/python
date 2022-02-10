from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question

def index(request):
    '''
    pybo 목록 출력
    '''
    # 입력 파라미터
    # http://localhost:8000/pybo/?page=1 처럼 GET 방식으로 호출된 URL에서 page값을 가져올 때 사용한다. 만약 http://localhost:8000/pybo/ 처럼 page값 없이 호출된 경우에는 디폴트로 1이라는 값을 설정한다.
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    question_list = Question.objects.order_by('-create_date')  # 내림차순 정렬

    # 페이징처리
    # cf) 페이징처리를 위해 장고셸에서 테스트데이터 한 번에 넣기: https://wikidocs.net/71240
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)  # 이렇게 하면 장고 내부적으로는 데이터 전체를 조회하지 않고 해당 페이지의 데이터만 조회하도록 쿼리가 변경된다.
    # cf)page_obj에 있는 속성들 - 템플릿에서 페이징 처리 시 사용: https://wikidocs.net/71240
    
    context = {'question_list': page_obj}

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