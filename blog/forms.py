from django import forms
from .models import ClassSchedule, Teacher


class ClassScheduleForm(forms.ModelForm):
    Subject_Choices = (
        ('Math', 'Mathematics'),
        ('EVS', 'Science'),
        ('Eng', 'English'),
        ('Soc', 'Social'),
        ('Hin', 'Hindi')
    )

    sub_name = forms.ChoiceField(
        choices=Subject_Choices,
        widget=forms.RadioSelect,
    )

    def grade_choices():
        return [(str(i), f'Grade {i}') for i in range(1, 10)]

    grade = forms.ChoiceField(
        choices= grade_choices,
        widget=forms.RadioSelect,
    )


    class Meta:
        model = ClassSchedule
        fields = '__all__'


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
