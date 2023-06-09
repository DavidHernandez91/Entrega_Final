"""Entrega_Final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from NewHome.views import (index, PropiedadesList, PropiedadesDetail, PropiedadesCreate, PropiedadesUpdate, 
                          PropiedadesDelete, SignUp, Login, Logout, ProfileUpdate, ProfileCreate, about, MensajeCreate, MensajeDelete, MensajeList)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('propiedades/create', PropiedadesCreate.as_view(), name="propiedades-create"),
    path('propiedades/list', PropiedadesList.as_view(), name="propiedades-list"),
    path('propiedades/<pk>/detail', PropiedadesDetail.as_view(), name="propiedades-detail"),
    path('propiedades/<pk>/update', PropiedadesUpdate.as_view(), name="propiedades-update"),
    path('propiedades/<pk>/delete', PropiedadesDelete.as_view(), name="propiedades-delete"),
    path('signup/',SignUp.as_view(), name="signup"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('profile/create', ProfileCreate.as_view(), name="profile-create"),
    path('profile/<pk>/update', ProfileUpdate.as_view(), name="profile-update"),
    path('AboutMe', about, name="AboutMe"),
    path('mensaje/create', MensajeCreate.as_view(), name="mensaje-create"),
    path('mensaje/list', MensajeList.as_view(), name="mensaje-list"),
    path('mensaje/<pk>/delete', MensajeDelete.as_view(), name="mensaje-delete"),
    

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
