"""
URL configuration for General project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from unicodedata import name
from django.urls import path
####### Importes para subir imágenes #######
from django.conf import settings
from django.conf.urls.static import static
############################################
from General.views import  inicio, sedes, servicios, clinica1, clinica2, clinica3, politica, certificacion, notas

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", inicio , name="inicio"),
    path('sedes', sedes , name="sedes"),
    path('servicios', servicios , name="servicios"),
    path('clinica1', clinica1 , name="clinica1"),
    path('clinica2', clinica2 , name="clinica2"),
    path('clinica3', clinica3 , name="clinica3"),
    path('politica', politica , name="politica"),
    path('certificacion', certificacion , name="certificacion"),
    path('notas', notas , name="notas"),
]
