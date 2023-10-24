from django.db import models


class ClassSchedule(models.Model):
    sub_name = models.CharField(max_length=50, default="Unknown")
    grade = models.CharField(max_length=50, default="Unknown")
    duration = models.IntegerField(default=0)

