from django.db import models

# Create your models here.

# CRUD - Create Read Update Delete
# agar Student.objects.create(name="Doniyorbek", content="Doniyorbek stikerlik laptop egasi") orqali create qilsa o'zi avtossave qiladi
# tenglash uchun Student3 = - qilsak bo'ldi
# CREATE
# student2 = Student()
# student2.name = "Diyorbek"
# student2.content = "ofbwoebrvobo"
# READ
# students = Student.objects.all()
# >>> students
# <QuerySet [<Student: Student object (1)>, <Student: Student object (2)>, <Student: Student object (3)>]>
# ############
# for student in students:
# ...     print(student)

# UPDATE
# student = Student.objects.update(is_active=0)
# >>> student
#  student = Student.objects.filter(pk=1).update(is_active=1)

# student = Student.objects.get(pk=1)    
# >>> student.name = "Tarixchi"
# >>> student.save()
# DELETE
# Student.objects.filter(pk=1).delete()

class Student(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
# students = Student.objects.all() qilganda ismi chiqishi uchun kerak
def __str__(self):
    return self.name