from django.urls import path
from cuidar import views


urlpatterns=[
             path("",views.cuidar,name="Cuidar")
]