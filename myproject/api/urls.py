from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add', views.addItem),
    path('detail/<str:pk>', views.oneData)
]
