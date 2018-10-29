from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<path:ymd>', views.date, name='index'),
]
