# index/urls.py
from django.urls import include, path
from . import views, views_ajax_custom, views_ajax_index
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('custom/get_settings', views_ajax_custom.get_settings, name='custom_get_settings'),
    path('custom/get_settings_summary', views_ajax_custom.get_settings_summary, name='custom_get_settings_summary'),
    path('custom/get_settings_data', views_ajax_custom.get_settings_data, name='custom_get_settings_data'),
    path('custom/get_matched_data', views_ajax_custom.get_matched_data, name='custom_get_matched_data'),
    path('custom/get_quiz_video_info', views_ajax_custom.get_quiz_video_info, name='custom_get_quiz_video_info'),
    path('custom/get_commercial_info', views_ajax_custom.get_commercial_info, name='custom_get_commercial_info'),
    path('index/get_settings', views_ajax_index.get_settings, name='index_get_settings'),
    path('index/get_settings_chart_data', views_ajax_index.get_chart_data, name='index_get_chart_data'),
    path('index/get_initial_commercial_data', views_ajax_index.get_initial_commercial_data, name='index_get_initial_commercial_data'),
    path('index/get_commercial_search_data', views_ajax_index.get_commercial_search_data, name='index_get_commercial_search_data'),
]