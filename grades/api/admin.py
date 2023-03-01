from django.contrib import admin
from .models import Student, Test, Question, StudentAnswer

class StudentAdmin(admin.ModelAdmin):
    # Defines how Student objects are displayed in the admin panel
    list_display = ('user', 'address', 'whatsapp')
    
    # Specifies fields to search for when filtering Student objects
    search_fields = ('user__first_name', 'user__last_name', 'address', 'whatsapp')
    
    # Specifies fields that should be read-only in the admin panel (commented out)
    # readonly_fields = ('user',)

class TestAdmin(admin.ModelAdmin):
    pass

class QuestionAdmin(admin.ModelAdmin):
    pass

class StudentAnswerAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        # Get the queryset of StudentAnswer objects
        qs = super().get_queryset(request)
        
        # If the user is a superuser, allow them to see all StudentAnswer objects
        if request.user.is_superuser:
            return qs
        
        # If the user is not a superuser, only allow them to see their own StudentAnswer objects
        return qs.filter(student__user=request.user)

# Register each model with its corresponding admin class
admin.site.register(StudentAnswer, StudentAnswerAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
