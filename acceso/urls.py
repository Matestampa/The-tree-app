from django.urls import path
from acceso import views

urlpatterns=[
             path("login/",views.login_view,name="Acceso_login"),
             path("signup/",views.signup_view,name="Acceso_signup")
]