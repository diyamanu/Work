from django import forms
from .models import ClassSchedule


class ClassScheduleForm(forms.ModelForm):
    class Meta:
        model = ClassSchedule
        fields = '__all__'
