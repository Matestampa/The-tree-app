from django.urls import path
from cuidar import views


urlpatterns=[
             path("all_trees",views.all_trees,name="Cuidar_tree")
]