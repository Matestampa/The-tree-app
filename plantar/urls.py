from django.urls import path
from plantar import views


urlpatterns=[
             path("new_tree/",views.new_tree,name="New_Tree")
]