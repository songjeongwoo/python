from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

# request.user를 사용하는 함수에 @login_required 데코레이터를 사용해야 한다.
@login_required(login_url='common:login')  # 로그아웃 상태에서 호출되면 자동으로 로그인 화면으로 이동시킨다.
def answer_create(request, question_id):
    '''
    pybo 답변등록
    '''
    question = get_object_or_404(Question, pk=question_id)
    '''
    수정 전 코드
    # Question과 Answer 모델은 서로 ForeignKey 로 연결되어 있기때문에 question.answer_set.create()처럼 사용할 수 있다.
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # 또는 아래처럼도 가능하다.
    # answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    # answer.save()
    return redirect('pybo:detail', question_id=question.id)
    '''
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # author 속성에 로그인 계정 저장  # request.user는 현재 로그인한 계정의 User 모델 객체
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:  # 사실 답변 등록은 POST 방식만 사용되기 때문에 if .. else 구문에서 else는 호출되지 않는다. 다만, 여기에서는 패턴의 통일성을 위해 남겨 두었다.
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)


@login_required(login_url='common:login')
def question_create(request):
    '''
    pybo 질문등록
    '''
    if request.method == 'POST':
        # request.POST를 인수로 QuestionForm을 생성할 경우에는 request.POST에 담긴 subject, content 값이 QuestionForm의 subject, content 속성에 자동으로 저장되어 객체가 생성된다.
        form = QuestionForm(request.POST)
        if form.is_valid():  # form에 저장된 subject, content의 값이 올바르지 않다면 form에는 오류 메시지가 저장되고 form.is_valid()가 실패하여 다시 질문 등록 화면으로 돌아간다.
            question = form.save(commit=False) # QuestionForm이 Question 모델과 연결된 모델 폼이기 때문에 이와 같이 사용할 수 있다. 여기서 commit=False는 임시 저장을 의미한다.
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    '''
    pybo 질문수정
    '''
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다.')  # messages는 장고가 제공하는 모듈로 넌필드 오류(non-field error)를 발생시킬 경우에 사용
        return redirect('pybo:detail', question_id=question.id)

    if request.method == "POST":
        # instance를 기준으로 QuestionForm을 생성하지만 request.POST의 값으로 덮어쓰라는 의미이다. 따라서 질문 수정화면에서 제목 또는 내용을 변경하여 POST 요청하면 변경된 내용이 QuestionForm에 저장된다.
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)  # instance 값을 지정하면 폼의 속성 값이 instance의 값으로 채워진다. instance=question을 안 써주면 수정화면에서 제목과 내용이 출력되지 않는다.
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    '''
    pybo 질문삭제
    '''
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    '''
    pybo 답변수정
    '''
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('pybo:detail', question_id=answer.question_id)
    
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('pybo:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    '''
    pybo 답변삭제
    '''
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다.')
    else:
        answer.delete()
    return redirect('pybo:detail', question_id=answer.question.id)