from django.db import models

# Create your models here.
class University(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    university = models.ForeignKey(University, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
