from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect
from aplikasi1.models import AccountUser

@receiver(post_save, sender=AccountUser, dispatch_uid="nim")
def check_nim(sender, instance, created, **kwargs):
    get_student_number = AccountUser.objects.filter(account_user_student_number=instance.account_user_student_number)
    get_email = User.objects.filter(username=instance.account_user_related_user.email)

    if get_student_number or get_email:
        return HttpResponse("Nim / email Telah digunakan!")
    else:
        if not created:
            User.objects.create(
                username=instance.account_user_related_user.email,
            )
            AccountUser.objects.create(
                account_user_fullname=instance.account_user_fullname,
                account_user_student_number=instance.account_user_student_number,
            )
        else:
            return HttpResponse("Error input Data")
        

@receiver(post_save, sender=AccountUser, dispatch_uid="nim")
def check_nim(sender, instance, created, **kwargs):
    if not created:
        get_student_number = AccountUser.objects.filter(Q(account_user_student_number=instance.nim))
        get_email = User.objects.filter(Q(username=instance.nim))

        if get_student_number or get_email:
            return HttpResponse('Data Exist')

        User.objects.create(
            username=instance.email) 
        AccountUser.objects.create(
            account_user_related_user=instance.email,            
            account_user_fullname=instance.fullname,           
            account_user_student_number=instance.nim
        )
    else:
        return redirect('aplikasi1:create-data-student')