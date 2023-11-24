from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(blank=True)
    enrolled_courses = models.ManyToManyField('Course', related_name='enrolled_users', blank=True)

    def __str__(self):
        return self.username

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    professor = models.ForeignKey("User", on_delete=models.CASCADE,default=None)
    lessons = models.ManyToManyField('Lesson', related_name='courses', blank=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=None)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assignments = models.ManyToManyField('Assignment', related_name='lessons', blank=True)
    

    def __str__(self):
        return self.title
class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    dueDay = models.DateField()
    deadline = models.TimeField()
    lesson = models.ForeignKey('Lesson',on_delete=models.CASCADE)
    def __str__(self):
        return self.title


