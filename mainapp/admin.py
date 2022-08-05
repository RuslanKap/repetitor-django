from django.contrib import admin

# Register your models here.
from app.models import Student, Course, HomeWork, HomeWorkStudent

admin.site.register(Student)
#admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(HomeWork)
admin.site.register(HomeWorkStudent)
