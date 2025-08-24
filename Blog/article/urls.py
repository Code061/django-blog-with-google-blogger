from django.urls import path
from article import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result/<str:id>/',views.result, name='result'),
]
