# index/urls.py
from django.urls import include, path
from . import views, views_ajax
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('custom', views.user_index, name="user_index"),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_out', views.sign_out, name='sign_out'),
    path('SignUp', views.SignUp.as_view(), name='SignUp'),
    path('UpdateProfile', views.UpdateProfile.as_view(), name='UpdateProfile'),
    path('check_duplicate_username', views_ajax.check_duplicate_username, name='check_duplicate_username'),
    path('check_duplicate_email', views_ajax.check_duplicate_email, name='check_duplicate_email'),
    path('dashboard/', include('dashboard.urls')),

    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]