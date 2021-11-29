from django.urls import path
from perfil import views

urlpatterns=[
             path("particular/<str:id>/",views.particular_profile,name="Perfil general"),
]