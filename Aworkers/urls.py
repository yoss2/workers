from django.urls import path
from . import views

urlpatterns = [
    path('', views.workers,name = 'workers'),
    path('workers1/<str:pk>/', views.workers1,name = 'workers1'),
]
