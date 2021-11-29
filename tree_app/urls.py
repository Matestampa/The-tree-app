from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("acceso/",include("acceso.urls")),
    path('home/',include("home.urls")),
    path("plantar/",include("plantar.urls")),
    path("cuidar/",include("cuidar.urls")),
    path("perfil/",include("perfil.urls"))
]
