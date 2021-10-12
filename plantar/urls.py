from django.urls import path
from plantar import views


urlpatterns=[
             path("",views.plantar,name="Plantar")
]