from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from client.models import Settings, TargetAge, TargetGender, TargetInterest, TargetLocation
from commercial.models import Quiz, QuizChoices, Video, TargetRecord, TargetAgeMatched, TargetInterestMatched, TargetGenderMatched, TargetLocationMatched
from django.core import serializers
from django.db.models import Count
from django.db.models.functions import TruncDay

def get_settings(request):
    client_id =  User.objects.filter(username = request.user)[0].id
    settings = Settings.objects.filter(info_id = client_id)
    context = {
        'settings_list': settings
    }
    return render(request, 'dashboard/custom/settings_initial.html', context)

def get_quiz_video_info(request):
    settings_id = request.POST.get('settings_id', None)
    quiz_list = Quiz.objects.filter(settings_id = settings_id)
    video_list = Video.objects.filter(settings_id = settings_id)
    return render(request, 'dashboard/custom/settings_quiz_video.html', {
        'quiz_list': quiz_list,
        'video_list': video_list
        })


def get_settings_summary(request):

    settings_id = request.POST.get('settings_id', None)
    print(settings_id)
    if settings_id == -1:
        settings = null
    else :
        settings = Settings.objects.filter(id = settings_id)


    target_l = TargetLocation.objects.filter(settings_id = settings_id)
    target_g = TargetGender.objects.filter(settings_id = settings_id)
    target_i = TargetInterest.objects.filter(settings_id = settings_id)
    target_a = TargetAge.objects.filter(settings_id = settings_id)
    
    context = {
        'settings_list': settings,
        'target_a':target_a,
        'target_i':target_i,
        'target_l': target_l,
        'target_g': target_g
        }

    return render(request, 'dashboard/custom/settings_summary.html', context)

def get_settings_data(request):
    settings_id = request.POST.get('settings_id', None)
    start_dt = request.POST.get('start_dt', None)
    end_dt = request.POST.get('end_dt', None)
    settings_data = TargetRecord.objects.all().select_related('quiz', 'quiz__settings').filter(quiz__settings__id=settings_id, date_at__range = [start_dt, end_dt]).values('date_at', 'quiz_id').annotate(tot_cnt = Count('date_at'))
    quiz_list = Quiz.objects.all().filter(settings_id=settings_id).values()
    context = {
        'settings_data': list(settings_data),
        'quiz_list' : list(quiz_list)
    }
    return JsonResponse(context, status=200)


def get_matched_data(request):
    settings_id = request.POST.get('settings_id', None)
    start = request.POST.get('start', None)
    end = request.POST.get('end', None)

    matched_age = TargetAgeMatched.objects.all().select_related('target_record','target_record__quiz', 'target_record__quiz__settings').filter(target_record__quiz__settings__id=settings_id, target_record__date_at__range = ['2020-11-05', '2020-11-24']).values('matched_age').annotate(tot_cnt = Count('matched_age'))
    matched_interest = TargetInterestMatched.objects.all().select_related('target_record','target_record__quiz', 'target_record__quiz__settings').filter(target_record__quiz__settings__id=settings_id, target_record__date_at__range = ['2020-11-05', '2020-11-24']).values('matched_interest').annotate(tot_cnt = Count('matched_interest'))
    matched_gender = TargetGenderMatched.objects.all().select_related('target_record','target_record__quiz', 'target_record__quiz__settings').filter(target_record__quiz__settings__id=settings_id, target_record__date_at__range = ['2020-11-05', '2020-11-24']).values('matched_gender').annotate(tot_cnt = Count('matched_gender'))
    matched_location = TargetLocationMatched.objects.all().select_related('target_record','target_record__quiz', 'target_record__quiz__settings').filter(target_record__quiz__settings__id=settings_id, target_record__date_at__range = ['2020-11-05', '2020-11-24']).values('matched_location').annotate(tot_cnt = Count('matched_location'))

    context = {
        'matched_age' : list(matched_age),
        'matched_interest' : list(matched_interest),
        'matched_gender' : list(matched_gender),
        'matched_location' : list(matched_location)
    }
    return JsonResponse(context, status=200)

def get_commercial_info(request):
    settings_id = request.POST.get('settings_id', None)

    settings = Settings.objects.filter(id=settings_id)

    target_l = TargetLocation.objects.filter(settings_id = settings_id)
    target_g = TargetGender.objects.filter(settings_id = settings_id)
    target_i = TargetInterest.objects.filter(settings_id = settings_id)
    target_a = TargetAge.objects.filter(settings_id = settings_id)

    context = {
        'status' : 200,
        'settings': settings,
        'target_l': target_l,
        'target_g': target_g,
        'target_i': target_i,
        'target_a': target_a
    }

    
    return render(request=request,template_name='dashboard/custom.html',context=context)
