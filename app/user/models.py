from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from client.models import TargetAge, TargetInterest, TargetGender, TargetLocation

# Create your models here.


class Info(models.Model):
    USER_ACTIVE = 'A'
    USER_INACTIVE = 'I'

    USER_STATUS = [
        (USER_ACTIVE, 'ACTIVE'),
        (USER_INACTIVE, 'INACTIVE')
    ]

    user_status = models.CharField(
        max_length=1,
        default=USER_ACTIVE,
        choices=USER_STATUS
    )
    email = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=50, null=True)
    bank_type = models.CharField(max_length=30, null=True)
    account_number = models.CharField(max_length=70, null=True)
    age = models.IntegerField(null=True)
    reg_at = models.DateField(default=timezone.now)


class Interest(models.Model):
    '''
    INTEREST SUB-CATEGORY SHOULD BE CONSIDERED FOR CLIENT PREFERENCE AT A LATER STAGE OF THE catchya-app development.
    Users of the app should only be able to choose INTEREST MAIN-CATEGORY for ease of completion.
    '''
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    interest = models.CharField(
        max_length=2,
        default=TargetInterest.INTEREST_MAIN_NONE,
        choices=TargetInterest.INTEREST_MAIN_CHOICES
    )


class AgeGroup(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    age = models.CharField(
        max_length=2,
        default=TargetAge.AGE_GROUP_0,
        choices=TargetAge.AGE_GROUP_CHOICES
    )


class Gender(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=2,
        default=TargetGender.GENDER_0,
        choices=TargetGender.GENDER_CHOICES
    )


class Location(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    location = models.CharField(
        max_length=2,
        default=TargetLocation.LOCATION_0,
        choices=TargetLocation.LOCATION_CHOICES
    )
    

class LoginInfo(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    login_ip = models.CharField(max_length=50)    
    last_login_at = models.DateField(default=timezone.now)






