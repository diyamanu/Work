from django.shortcuts import render, redirect
from blog.models import ClassSchedule, Teacher
from blog.forms import ClassScheduleForm, TeacherForm


def welcome(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return index(request)  # Redirect to the next attribute page
    return render(request, "welcome.html", {'form': form})


def index(request):
    form = Teacher.objects.order_by('-id').first()
    return render(request, "index.html", {'form': form})


def listclass(request):
    classes = ClassSchedule.objects.order_by('-id').first()
    return render(request, "listclass.html", {'classes': classes})


def addclass(request):
    form = ClassScheduleForm()
    if request.method == 'POST':
        form = ClassScheduleForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return listclass(request)
    return render(request, "addclass.html", {'form': form})

def deleteclass(request):
    form = ClassScheduleForm()
    if request.method == 'POST':
        classes = ClassSchedule.objects.latest('id')
        classes.delete()
        #form.save()
        return redirect('success')
    return render(request, "deleteclass.html")

def success(request):
    return render(request, "success.html")