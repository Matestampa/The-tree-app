from django.urls import path
from plantar import views


urlpatterns=[
             path("",views.all_trees,name="Plantar")
]