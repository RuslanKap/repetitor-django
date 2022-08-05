
from django.db import models



class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slag = models.SlugField(max_length=255, unique=True)
    foto = models.ImageField(upload_to='courses_foto/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'course'
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'




class HomeWork(models.Model):
    title = models.CharField(max_length=255)
    home_work_data = models.TextField(blank=True, null=True)
    solution = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    updated_at = models.DateField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, blank=True, null=True)  # Field renamed because it started with '_'.

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'home_work'
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашние задания'


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    telegram_id = models.CharField(max_length=255)
    course = models.ManyToManyField(Course,  blank=True)
    created_at = models.DateField(auto_now_add=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    updated_at = models.DateField(auto_now=True)
    foto = models.ImageField(upload_to='students_foto/%Y/%m/%d', blank=True, default='students_foto/default.png')

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'student'
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class HomeWorkStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    home_work = models.ForeignKey(HomeWork, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    updated_at = models.DateField(auto_now=True)
    is_assigned = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.student.first_name + ' - ' + self.home_work.title

    class Meta:
        db_table = 'home_work_student'
        verbose_name = 'Домашнее задание студента'
        verbose_name_plural = 'Домашнее задание студентов'