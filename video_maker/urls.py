from django.urls import path
from . import views


urlpatterns = [
    path('video_maker/', views.VideoTemplateView.as_view(), name='video_maker'),

]