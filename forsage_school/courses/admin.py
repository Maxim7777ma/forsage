from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('title', 'description', 'start_date', 'duration')  

admin.site.register(Course, CourseAdmin)
=======
    list_display = ('title', 'description', 'start_date', 'duration')  # Отображаемые поля в админ-панели

admin.site.register(Course, CourseAdmin)
>>>>>>> 79c4817e39626633e9d58ce9a1eb13dec6e8c871
