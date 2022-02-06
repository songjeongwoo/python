from django.contrib import admin
from .models import Question

# 관리자 화면에 검색기능 추가
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

# admin.site.register(Question)
admin.site.register(Question, QuestionAdmin)


# cf) 장고 관리자 기능: https://docs.djangoproject.com/en/3.0/ref/contrib/admin/