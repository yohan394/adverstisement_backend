from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from client.models import Settings
from django.utils import timezone
# Create your models here.


class Video(models.Model):
    settings = models.ForeignKey(Settings, on_delete=models.CASCADE)
    file = models.FileField(upload_to='videos/')

    IS_USED_NO = 'N'
    IS_USED_YES = 'Y'

    IS_USED_CHOICES = [
        (IS_USED_YES, '사용'),
        (IS_USED_NO, '사용안함'),
    ]
    is_used = models.CharField(
        max_length=1,
        choices=IS_USED_CHOICES,
        default=IS_USED_YES,
    )


class Quiz(models.Model):
    settings = models.ForeignKey(Settings, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    IS_USED_NO = 'N'
    IS_USED_YES = 'Y'

    IS_USED_CHOICES = [
        (IS_USED_YES, '사용'),
        (IS_USED_NO, '사용안함'),
    ]
    is_used = models.CharField(
        max_length=1,
        choices=IS_USED_CHOICES,
        default=IS_USED_YES,
    )


class QuizChoices(models.Model):
    IS_CORRECT_YES = 'Y'
    IS_CORRECT_NO = 'N'

    IS_CORRECT_CHOICES = [
        (IS_CORRECT_YES, '정답'),
        (IS_CORRECT_NO, '오답'),
    ]

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    choice = models.CharField(max_length=300)
    is_correct = models.CharField(
        max_length=1,
        choices=IS_CORRECT_CHOICES,
        default=IS_CORRECT_YES,
    )


class TargetRecord(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    date_at = models.DateField(default=timezone.now)

class TargetAgeMatched(models.Model):
    target_record = models.ForeignKey(TargetRecord, on_delete=models.CASCADE)
    matched_age = models.CharField(max_length=10) 

class TargetInterestMatched(models.Model):
    target_record = models.ForeignKey(TargetRecord, on_delete=models.CASCADE)
    matched_interest = models.CharField(max_length=50)

class TargetGenderMatched(models.Model):
    target_record = models.ForeignKey(TargetRecord, on_delete=models.CASCADE)
    matched_gender = models.CharField(max_length=10)

class TargetLocationMatched(models.Model):
    target_record = models.ForeignKey(TargetRecord, on_delete=models.CASCADE)
    matched_location = models.CharField(max_length=30)

class TargetAgeUnmatched(models.Model):
    target_record = models.ForeignKey(TargetRecord, on_delete=models.CASCADE)
    matched_age = models.CharField(max_length=10) 

class TargetInterestUnmatched(models.Model):
    target_record = models.ForeignKey(TargetRecord, on_delete=models.CASCADE)
    matched_interest = models.CharField(max_length=50)

class TargetGenderUnmatched(models.Model):
    target_record = models.ForeignKey(TargetRecord, on_delete=models.CASCADE)
    matched_gender = models.CharField(max_length=10)

class TargetLocationUnmatched(models.Model):
    target_record = models.ForeignKey(TargetRecord, on_delete=models.CASCADE)
    matched_location = models.CharField(max_length=30)