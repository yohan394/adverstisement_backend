from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from client.models import Settings, TargetAge, TargetGender, TargetInterest, TargetLocation
from treasure.models import *
from user.models import *
from django.core import serializers
from django.db.models import Count, Sum
from django.db.models.functions import TruncDay
from django.utils.encoding import force_text
import datetime


# Create your views here.
def get_settings(request):

    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)

    quiz_info = TransactionQuiz.objects.filter(date_at__range=[today_min, today_max]).values('date_at').annotate(tot_cnt = Count('date_at'), tot_reward = Sum('rewarded'))
    video_info = TransactionVideo.objects.filter(date_at__range=[today_min, today_max]).values('date_at').annotate(tot_cnt = Count('date_at'), tot_reward = Sum('rewarded'))

    reward_cap_info = RewardCap.objects.filter(date_at__range=[today_min, today_max]).values()

    user_info = Info.objects.filter(reg_at__range=[today_min, today_max]).values('reg_at').annotate(tot_cnt = Count('reg_at'))
    login_info = LoginInfo.objects.filter(last_login_at__range=[today_min, today_max]).values('last_login_at').annotate(tot_cnt = Count('last_login_at'))

    context = {
        'quiz_info': list(quiz_info),
        'video_info': list(video_info),
        'reward_cap_info': list(reward_cap_info),
        'user_info' : list(user_info),
        'login_info' : list(login_info)
    }

    return JsonResponse(context, status=200)

def get_chart_data(request):
    
    start_dt = request.POST.get('start_dt', None)
    end_dt = request.POST.get('end_dt', None)

    quiz_info = TransactionQuiz.objects.filter(date_at__range=[start_dt, end_dt]).values('date_at').annotate(tot_cnt = Count('date_at'), tot_reward = Sum('rewarded')).order_by('date_at')
    video_info = TransactionVideo.objects.filter(date_at__range=[start_dt, end_dt]).values('date_at').annotate(tot_cnt = Count('date_at'), tot_reward = Sum('rewarded')).order_by('date_at')

    reward_cap_info = RewardCap.objects.filter(date_at__range=[start_dt, end_dt]).values().order_by('date_at')

    user_info = Info.objects.filter(reg_at__range=[start_dt, end_dt]).values('reg_at').annotate(tot_cnt = Count('reg_at'))
    existing_user = Info.objects.filter(reg_at__lt=start_dt).count()
    login_info = LoginInfo.objects.filter(last_login_at__range=[start_dt, end_dt]).values('last_login_at').annotate(tot_cnt = Count('last_login_at'))



    context = {
        'quiz_info': list(quiz_info),
        'video_info': list(video_info),
        'reward_cap_info': list(reward_cap_info),
        'user_info' : list(user_info),
        'existing_user' : existing_user,
        'login_info' : list(login_info)
    }

    return JsonResponse(context, status=200)

def get_initial_commercial_data(request):

    age_info = AgeGroup.objects.values('age').annotate( tot_cnt = Count('age')).order_by('age')
    location_info = Location.objects.values('location').annotate(tot_cnt = Count('location'))
    interest_info = Interest.objects.values('interest').annotate(tot_cnt = Count('interest'))
    gender_info = Gender.objects.values('gender').annotate(tot_cnt = Count('gender'))
    
    context = {
        'age': TargetAge.AGE_GROUP_CHOICES,
        'gender': TargetGender.GENDER_CHOICES,
        'interest': TargetInterest.INTEREST_MAIN_CHOICES,
        'location' : TargetLocation.LOCATION_CHOICES,
        'data' : {
            'age' : list(age_info),
            'location' : list(location_info),
            'interest' : list(interest_info),
            'gender' : list(gender_info),
        }
    }

    return JsonResponse(context, status=200)

def get_commercial_search_data(request):
    age_filter = request.POST.getlist('age_list[]',[])
    location_filter = request.POST.getlist('location_list[]', [])
    gender_filter = request.POST.getlist('gender_list[]', [])
    interest_filter = request.POST.getlist('interest_list[]', [])

    filtered = Info.objects

    if(len(age_filter)>0): 
        filtered = filtered.filter(agegroup__age__in=age_filter)
    if(len(interest_filter)>0):
        filtered = filtered.filter(interest__interest__in=interest_filter)
    if(len(gender_filter)>0):
        filtered = filtered.filter(gender__gender__in=gender_filter)
    if(len(location_filter)>0):
        filtered = filtered.filter(location__location__in=location_filter)
    
    context = { 
        'targeted_count' : filtered.all().count(),
    }

    return JsonResponse(context, status=200)