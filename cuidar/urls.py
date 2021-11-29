from django.urls import path
from cuidar import views


urlpatterns=[
             path("all_trees",views.all_trees,name="Get_trees"),
             path("take_tree",views.take_tree,name="Cuidar_arbol"),
             path("confirm",views.confirm,name="Confirma cuidado")
]