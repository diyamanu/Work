from django.db import models


class ClassSchedule(models.Model):

    sub_name = models.CharField(max_length=50, default="Unknown")
    grade = models.CharField(max_length=50, default="Unknown")
    duration = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.sub_name} (Grade: {self.grade}, Duration: {self.duration} minutes)"


class Teacher(models.Model):
    teacher = models.CharField(max_length=50, default="Unknown")
    password = models.CharField(max_length=50, default="Unknown")

    def __str__(self):
        return f"{self.teacher} (Password: {self. password})"

