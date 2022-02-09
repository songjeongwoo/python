from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    # User모델은 django.contrib.auth앱이 제공하는 사용자 모델이다. cf) author 속성 추가 후 makemigrations를 하면 오류 - 해결방법: https://wikidocs.net/71306
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # author 속성에 저장해야 하는 사용자 객체는 로그인 후 request 객체를 통해 얻을 수 있다.
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)  # blank=True는 form.is_valid()를 통한 입력 데이터 검사 시 값이 없어도 된다는 의미

    def __str__(self):
        return self.subject
        # <Question: Question object (1)>를 <Question: pybo가 무엇인가요?>로 출력되게 해줌

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Question의 author 설명과 동일
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)  # blank=True는 form.is_valid()를 통한 입력 데이터 검사 시 값이 없어도 된다는 의미

    # 장고에서 사용하는 속성(Field) 타입: https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-types

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
    # 만약 질문에 댓글이 작성될 경우에는 question에 값이 저장되고 답변에 댓글이 작성될 경우에는 answer에 값이 저장될 것이다.
    # 따라서 댓글 모델의 question 또는 answer 둘 중에 하나에만 값이 저장되므로 두 개의 속성은 모두 null=True, blank=True 를 설정해야 한다.

'''
# 장고 셸 실행
(mysite) c:\projects\mysite>python manage.py shell

## Question 생성
>>> from pybo.models import Question, Answer
>>> from django.utils import timezone
>>> q = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고 싶습니다.', create_date=timezone.now())
>>> q.save()
>>> q.id
1


## Question 조회
>>> Question.objects.all()
<QuerySet [<Question: pybo가 무엇인가요?>]>

>>> Question.objects.filter(id=1)
<QuerySet [<Question: pybo가 무엇인가요?>]>

>>> Question.objects.get(id=1)
<Question: pybo가 무엇인가요?>

>>> Question.objects.filter(subject__contains='장고')
<QuerySet [<Question: 장고 모델 질문입니다.>]>
# cf) filter사용법: https://docs.djangoproject.com/en/3.0/topics/db/queries/


## Question 수정
>>> q = Question.objects.get(id=2)
>>> q.subject = 'Django Model Question'
>>> q.save()
>>> q
<Question: Django Model Question>


## Question 삭제
>>> q = Question.objects.get(id=1)
>>> q.delete()
(1, {'pybo.Question': 1})


## Answer 작성
>>> q = Question.objects.get(id=2)
>>> q
<Question: Django Model Question>
>>> from django.utils import timezone
>>> a = Answer(question=q, content='네 자동으로 생성됩니다.', create_date=timezone.now())
>>> a.save()


## Answer로 연결된 Question 조회
>>> a.question
<Question: Django Model Question>


## Qustion으로 Answer 조회
>>> q.answer_set.all()
<QuerySet [<Answer: Answer object (1)>]>

cf)★★
연결모델명_set(예:answer_set)은 상식적으로 생각하면 더 쉽다.
질문 하나에는 여러개의 답변이 가능하므로 q.answer_set이 가능하지만,
답변 하나에는 여러개의 질문이 있을 수 없으므로 a.question_set은 불가능하다.
답변 하나에는 질문 하나만 가능하기 때문에 a.question만 가능하다.
'''