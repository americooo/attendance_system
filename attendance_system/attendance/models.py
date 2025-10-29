from django.db import models
from django.contrib.auth.models import User

# Talabalar jadvali
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username


# Davomat jadvali
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[
        ('Present', 'Present'),
        ('Absent', 'Absent')
    ])

    def __str__(self):
        return f"{self.student.user.username} - {self.date} - {self.status}"
