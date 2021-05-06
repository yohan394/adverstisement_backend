from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.


class Info(models.Model):
    REGISTRATION_APPROVED = 'A'
    REGISTRATION_PENDING = 'P'
    REGISTRATION_DENIED = 'D'
    REGISTRATION_UNREGISTERED = 'U'

    REGISTRATION_STATUS = [
        (REGISTRATION_APPROVED, 'APPROVED'),
        (REGISTRATION_PENDING, 'PENDING'),
        (REGISTRATION_DENIED, 'DENIED'),
        (REGISTRATION_UNREGISTERED, 'UNREGISTERED'),
    ]

    CLIENT_TYPE_BUSINESS = 'B'
    CLIENT_TYPE_INDIVIDUAL = 'I'

    CLIENT_TYPE_CHOICES = [
        (CLIENT_TYPE_BUSINESS, '법인'),
        (CLIENT_TYPE_INDIVIDUAL, '개인')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    client_type = models.CharField(
        max_length=1,
        default=CLIENT_TYPE_BUSINESS,
        choices=CLIENT_TYPE_CHOICES
    )

    mobile = models.CharField(max_length=50, null=True)
    business_name = models.CharField(max_length=100, null=True)
    business_number = models.CharField(max_length=50, null=True)
    registration_status = models.CharField(
        max_length=1,
        choices=REGISTRATION_STATUS,
        default=REGISTRATION_PENDING
    )


class Settings(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_DENIED = 'D'
    PAYMENT_REQUESTED = 'R'
    PAYMENT_APPROVED = 'A'
    PAYMENT_COMPLETED = 'C'

    PAYMENT_STATUS = [
        (PAYMENT_PENDING, 'PENDING'),
        (PAYMENT_REQUESTED, 'REQUESTING'),
        (PAYMENT_DENIED, 'DENIED'),
        (PAYMENT_APPROVED, 'APPROVED'),
        (PAYMENT_COMPLETED, 'COMPLETED'),
    ]

    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    target_size = models.IntegerField(default=1000)
    exposed_size = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    payment_status = models.CharField(
        max_length=1,
        choices=PAYMENT_STATUS,
        default=PAYMENT_PENDING
    )
    register_at = models.DateField(default=timezone.now)


class TargetInterest(models.Model):
    '''
    INTEREST SUB-CATEGORY SHOULD BE CONSIDERED FOR CLIENT PREFERENCE AT A LATER STAGE OF THE catchya-app development.
    Users of the app should only be able to choose INTEREST MAIN-CATEGORY for ease of completion.
    '''
    INTEREST_MAIN_NONE = 'NO'
    INTEREST_MAIN_SPORT = 'SP'
    INTEREST_MAIN_GAMES = 'GA'
    INTEREST_MAIN_MUSIC = 'MU'
    INTEREST_MAIN_MOVIES = 'MO'
    INTEREST_MAIN_TRAVEL = 'TR'
    INTEREST_MAIN_FOOD = 'FO'
    INTEREST_MAIN_SELF_IMPROVEMENT = 'SI'
    INTEREST_MAIN_DANCE = 'DA'
    INTEREST_MAIN_TECH = 'TE'
    INTEREST_MAIN_ANIMAL = 'AN'

    INTEREST_MAIN_CHOICES = [
        (INTEREST_MAIN_NONE, '없음'),
        (INTEREST_MAIN_SPORT, '스포츠'),
        (INTEREST_MAIN_GAMES, '게임'),
        (INTEREST_MAIN_MUSIC, '음악'),
        (INTEREST_MAIN_MOVIES, '영화'),
        (INTEREST_MAIN_TRAVEL, '여행'),
        (INTEREST_MAIN_FOOD, '음식'),
        (INTEREST_MAIN_SELF_IMPROVEMENT, '자기개발'),
        (INTEREST_MAIN_DANCE, '춤'),
        (INTEREST_MAIN_TECH, '기술'),
        (INTEREST_MAIN_ANIMAL, '동물'),
    ]

    settings = models.ForeignKey(Settings, on_delete=models.CASCADE)
    interest = models.CharField(
        max_length=2,
        default=INTEREST_MAIN_NONE,
        choices=INTEREST_MAIN_CHOICES
    )


class TargetAge(models.Model):
    AGE_GROUP_0 = 'A0'
    AGE_GROUP_10 = 'A1'
    AGE_GROUP_20 = 'A2'
    AGE_GROUP_30 = 'A3'
    AGE_GROUP_40 = 'A4'
    AGE_GROUP_50 = 'A5'
    AGE_GROUP_60 = 'A6'

    AGE_GROUP_CHOICES = [
        (AGE_GROUP_0, '상관없음'),
        (AGE_GROUP_10, '0~19'),
        (AGE_GROUP_20, '20~29'),
        (AGE_GROUP_30, '30~39'),
        (AGE_GROUP_40, '40~49'),
        (AGE_GROUP_50, '50~59'),
        (AGE_GROUP_60, '60+'),
    ]

    settings = models.ForeignKey(Settings, on_delete=models.CASCADE)
    age = models.CharField(
        max_length=2,
        default=AGE_GROUP_0,
        choices=AGE_GROUP_CHOICES
    )


class TargetGender(models.Model):
    GENDER_0 = 'G0'
    GENDER_M = 'GM'
    GENDER_F = 'GF'
    GENDER_CHOICES = [
        (GENDER_0, '상관없음'),
        (GENDER_M, '남'),
        (GENDER_F, '여'),
    ]

    settings = models.ForeignKey(Settings, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=2,
        default=GENDER_0,
        choices=GENDER_CHOICES
    )


class TargetLocation(models.Model):
    LOCATION_0 = 'L0'
    LOCATION_Seoul = 'L1'
    LOCATION_Gyeonggi = 'L2'
    LOCATION_Gangwon = 'L3'
    LOCATION_Chungcheong = 'L4'
    LOCATION_Gyeongsang = 'L5'
    LOCATION_Jeolla = 'L6'
    LOCATION_Jeju = 'L7'

    LOCATION_CHOICES = [
        (LOCATION_0, '상관없음'),
        (LOCATION_Seoul, '서울'),
        (LOCATION_Gyeonggi, '경기'),
        (LOCATION_Gangwon, '강원'),
        (LOCATION_Chungcheong, '충청'),
        (LOCATION_Gyeongsang, '경상'),
        (LOCATION_Jeolla, '전라'),
        (LOCATION_Jeju, '제주'),
    ]

    settings = models.ForeignKey(Settings, on_delete=models.CASCADE)
    location = models.CharField(
        max_length=2,
        default=LOCATION_0,
        choices=LOCATION_CHOICES
    )
    

