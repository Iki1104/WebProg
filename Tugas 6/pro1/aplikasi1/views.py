import sys
from unittest import loader
from django.contrib import messages
from django.db.models.signals import post_save
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from django.contrib.auth.models import User
from aplikasi1.models import AccountUser, Course, AttendingCourse
from aplikasi1.signals import check_nim
from aplikasi1.forms import StudentRegisterForm

# Create your views here.
def readStudent(request):
    data = AccountUser.objects.all()

    context = {'data_list': data}

    return render(request, 'home.html', context)


@csrf_protect
def createStudent(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            post_save.disconnect(check_nim)
            form.fullname = form.cleaned_data.get("fullname")
            form.nim = form.cleaned_data.get("nim")
            form.email = form.cleaned_data.get("email")
            post_save.send(
            sender=AccountUser, created=None,        instance=form,                dispatch_uid="check_nim")
            messages.success(request, 'Data Berhasil disimpan')
            return redirect('aplikasi1:read-data-student')
    else:
        form = StudentRegisterForm()

    return render(request, 'form.html', {'form': form})


@csrf_protect
def updateStudent(request, id):
    member = AccountUser.objects.get(account_user_related_user=id)
    user = User.objects.get(username=id)
    template = loader.get_template('update.html')
    context = {
        'member': member,
        'user' : user
    }   
    messages.success(request, 'Data Berhasil disimpan')
    return HttpResponse(template.render(context, request))

@csrf_protect
def updaterecord(request, id):
    student = AccountUser.objects.get(account_user_related_user=id)
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            student.account_user_fullname = form.cleaned_data.get("fullname")
            student.account_user_student_number = form.cleaned_data.get("nim")
            student.account_user_updated_by = request.user.username
            student.save()
            messages.success(request, 'Data Berhasil diupdate')
            return redirect('aplikasi1:read-data-student')
    else:
        form = StudentRegisterForm(initial={
            'fullname': student.account_user_fullname,
            'nim': student.account_user_student_number,
        })
    return render(request, 'form.html', {'form': form})


@csrf_protect
def deleteStudent(request, id):
    member = AccountUser.objects.get(account_user_related_user=id)
    user = User.objects.get(username=id)
    member.delete()
    user.delete()
    messages.success(request, 'Data Berhasil dihapus')
    return redirect('aplikasi1:read-data-student')

# Create your views here.
def home(request):
    return render(request, 'home.html')

def readCourse(request):
    data = Course.objects.all()[:1]  # Membatasi data (1 item)
    context = {'data_list': data}
    return render(request, 'course.html', context)

@csrf_protect
def createCourse(request):
    return render(request, 'home.html')

@csrf_protect
def updateCourse(request):
    return render(request, 'home.html')

@csrf_protect
def deleteCourse(request, id):
    try:
        data = Course.objects.filter(course_id=id)
        if data.exists():
            data.delete()
            messages.success(request, 'Data Berhasil dihapus')
        else:
            messages.success(request, 'Data Tidak ditemukan')
        return redirect('aplikasi1:read-data-course')
    except:
        return redirect('aplikasi1:read-data-course')

def readStudent(request):
    data = AccountUser.objects.all()
    context = {'data_list': data}
    return render(request, 'index.html', context)

@csrf_protect
def createStudent(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            post_save.disconnect(check_nim)
            form.fullname = form.cleaned_data.get("fullname")
            form.nim = form.cleaned_data.get("nim")
            form.email = form.cleaned_data.get("email")
            post_save.send(sender=AccountUser, created=None, instance=form, dispatch_uid="check_nim")
            messages.success(request, 'Data Berhasil disimpan')
            return redirect('aplikasi1:read-data-student')
    else:
        form = StudentRegisterForm()
    return render(request, 'form.html', {'form': form})

@csrf_protect
def updateStudent(request, id):
    messages.success(request, 'Data Berhasil disimpan')
    return redirect('aplikasi1:read-data-student')

@csrf_protect
def deleteStudent(request, id):
    try:
        member = AccountUser.objects.get(account_user_related_user=id)
        user = User.objects.get(username=id)
        member.delete()
        user.delete()
        messages.success(request, 'Data Berhasil dihapus')
    except AccountUser.DoesNotExist:
        messages.error(request, 'Data Tidak ditemukan')
    return redirect('aplikasi1:read-data-student')