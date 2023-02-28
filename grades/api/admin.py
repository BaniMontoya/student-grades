from django.contrib import admin
from .models import Student, Test, Question, Answer

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'whatsapp')
    search_fields = ('user__first_name', 'user__last_name', 'address', 'whatsapp')
    readonly_fields = ('user',)

class TestAdmin(admin.ModelAdmin):
    pass

class QuestionAdmin(admin.ModelAdmin):
    pass

class AnswerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, StudentAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
