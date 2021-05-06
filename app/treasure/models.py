from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from user.models import Info
from commercial.models import Quiz, QuizChoices, Video


class TransactionQuiz(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING)
    user_choice = models.ForeignKey(QuizChoices, on_delete=models.DO_NOTHING)
    rewarded = models.IntegerField()
    date_at = models.DateField(default=timezone.now)

class TransactionVideo(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.DO_NOTHING)
    rewarded = models.IntegerField()
    date_at = models.DateField(default=timezone.now)

class RewardCap(models.Model):
    date_at = models.DateField(default=timezone.now)
    daily_cap = models.IntegerField()

