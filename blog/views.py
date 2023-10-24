from django.shortcuts import render
from blog.models import ClassSchedule
from blog.forms import ClassScheduleForm


def index(request):
    return render(request, "index.html", {})


def listclass(request):
    classes = ClassSchedule.objects.all()
    return render(request, "listclass.html", {'classes': classes})


def addclass(request):
    form = ClassScheduleForm()
    if request.method == 'POST':
        form = ClassScheduleForm(request.POST)
        form.save()
        return index(request)
    return render(request, "addclass.html", {'form': form})
