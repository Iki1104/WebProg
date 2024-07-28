import sys
from django.contrib import messages
from django.db.models.signals import post_save
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from django.contrib.auth.models import User
from aplikasi1.models import AccountUser, Course, AttendingCourse
from aplikasi1.signals import check_nim
from aplikasi1.forms import StudentRegisterForm
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    return render(request, 'home.html')

def readCourse(request):
    # Mengambil data dari models.py yang Course
    data = Course.objects.all()
    konteks = {'data_list': data}
    return render(request, 'course.html', konteks)

def createCourse(request):
    return render(request, 'home.html')

def updateCourse(request):
    return render(request, 'home.html')

@csrf_protect
def deleteCourse(request, id):
    data = get_object_or_404(Course, course_id=id)
    if request.method == 'POST':
        data.delete()
        messages.success(request, 'Data berhasil dihapus')
        return redirect('aplikasi1:read-data-course')
    else:
        messages.error(request, 'Data tidak ada')
        return redirect('aplikasi1:read-data-course')

def readStudent(request):
    # Mengambil data dari models.py yang AccountUser
    data = AccountUser.objects.all()
    context = {'data_list': data}
    return render(request, 'index.html', context)

@csrf_protect
def createStudent(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            post_save.disconnect(check_nim)
            account_user = form.save(commit=False)
            account_user.fullname = form.cleaned_data.get("fullname")
            account_user.nim = form.cleaned_data.get("nim")
            account_user.email = form.cleaned_data.get("email")
            account_user.save()
            post_save.connect(check_nim, sender=AccountUser)
            messages.success(request, 'Data berhasil disimpan')
            return redirect('aplikasi1:read-data-student')
    else:
        form = StudentRegisterForm()
    return render(request, 'home.html', {'form': form})

@csrf_protect
def updateStudent(request, id):
    member = get_object_or_404(AccountUser, id=id)
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil diupdate')
            return redirect('aplikasi1:read-data-student')
    else:
        form = StudentRegisterForm(instance=member)
    return render(request, 'update.html', {'form': form})

@csrf_protect
def deleteStudent(request, id):
    member = get_object_or_404(AccountUser, id=id)
    user = get_object_or_404(User, username=member.account_user_related_user)
    if request.method == 'POST':
        member.delete()
        user.delete()
        messages.success(request, 'Data berhasil dihapus')
        return redirect('aplikasi1:read-data-student')
    else:
        messages.error(request, 'Data tidak ada')
        return redirect('aplikasi1:read-data-student')
