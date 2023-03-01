from django.contrib import admin
from .models import Student, Test, Question, StudentAnswer


class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'whatsapp')
    search_fields = ('user__first_name', 'user__last_name',
                     'address', 'whatsapp')
    # readonly_fields = ('user',)


class TestAdmin(admin.ModelAdmin):
    pass


class QuestionAdmin(admin.ModelAdmin):
    pass


class StudentAnswerAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(student__user=request.user)


admin.site.register(StudentAnswer, StudentAnswerAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
