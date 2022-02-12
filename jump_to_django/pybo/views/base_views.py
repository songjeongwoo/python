from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question
from django.db.models import Q, Count

def index(request):
    '''
    pybo 목록 출력
    '''
    # 입력 파라미터
    # http://localhost:8000/pybo/?page=1 처럼 GET 방식으로 호출된 URL에서 page값을 가져올 때 사용한다. 만약 http://localhost:8000/pybo/ 처럼 page값 없이 호출된 경우에는 디폴트로 1이라는 값을 설정한다.
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준

    ## 정렬 코드 전 조회
    # question_list = Question.objects.order_by('-create_date')

    # 정렬(조회)
    if so == 'recommend':  # annotate의 Count함수를 사용해서 추천수를 구한다. 이렇게 annotate로 num_voter를 지정하면 filter나 order_by에서 num_voter를 사용할 수 있게 된다.
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')  # 내림차순 정렬
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:  # recent
        question_list = Question.objects.order_by('-create_date')

    # 검색
    if kw:
        question_list = question_list.filter(  # filter 함수에서 모델 속성에 접근하기 위해서는 이처럼 __ (언더바 두개) 를 이용하여 하위 속성에 접근할 수 있다.
            # cf) subject__contains=kw 대신 subject__icontains=kw을 사용하면 대소문자를 가리지 않고 찾아 준다.
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

    # 페이징처리
    # cf) 페이징처리를 위해 장고셸에서 테스트데이터 한 번에 넣기: https://wikidocs.net/71240
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)  # 이렇게 하면 장고 내부적으로는 데이터 전체를 조회하지 않고 해당 페이지의 데이터만 조회하도록 쿼리가 변경된다.
    # cf)page_obj에 있는 속성들 - 템플릿에서 페이징 처리 시 사용: https://wikidocs.net/71240
    
    context = {'question_list': page_obj, 'page': page,  'kw': kw, 'so': so}  ## 'page':page는 안 넘겨줘도 작동 - 점프투장고에서 왜 써놨는지 모르겠음..

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