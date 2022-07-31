# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class HomeWork(models.Model):
    home_work_id = models.IntegerField(primary_key=True)
    home_work_data = models.TextField(blank=True, null=True)
    solution = models.TextField(blank=True, null=True)
    field_created_at = models.DateField(db_column=' created_at', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    updated_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home_work'


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255, blank=True, null=True)
    mail = models.CharField(max_length=255, blank=True, null=True)
    cousre = models.ForeignKey('TrainingCourse', models.DO_NOTHING, blank=True, null=True)
    cteate_at = models.DateField(blank=True, null=True)
    updated_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class TrainingCourse(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'training_course'
