from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import AnswerForm
from ..models import Question, Answer

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
            return redirect('{}#answer_{}'.format(
                resolve_url('pybo:detail', question_id=question.id), answer.id))  # pybo:detail에 해당하는 HTML 중 answer_answer.id 앵커로 이동한다.
    else:  # 사실 답변 등록은 POST 방식만 사용되기 때문에 if .. else 구문에서 else는 호출되지 않는다. 다만, 여기에서는 패턴의 통일성을 위해 남겨 두었다.
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

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
            return redirect('{}#answer_{}'.format(
                resolve_url('pybo:detail', question_id=answer.question.id), answer.id))  # pybo:detail에 해당하는 HTML 중 answer_answer.id 앵커로 이동한다.
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
