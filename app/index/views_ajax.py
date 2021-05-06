from django.http import JsonResponse
from django.contrib.auth.models import User


def check_duplicate_username(request):
    username = request.GET.get('username', None)

    if User.objects.filter(username=username).exists():
        return JsonResponse({'status': 'error', 'msg': 'This ID already exists. Try using different ID.'})
    else:
        return JsonResponse({'status': 'success', 'msg': 'you can use this ID.'})


def check_duplicate_email(request):
    email = request.GET.get('email', None)

    if User.objects.filter(email=email).exists():
        return JsonResponse({'status': 'error', 'msg': 'This email already exists. Try using different email.'})
    else:
        return JsonResponse({'status': 'success', 'msg': 'you can use this ID.'})