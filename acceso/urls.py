from django.urls import path
from acceso import views

urlpatterns=[
             path("login/",views.login,name="Acceso_login"),
             path("signup/",views.signup,name="Acceso_signup")
]