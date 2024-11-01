"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('example/',example,name='example'),
    path('first/',first,name='first'),
    path('insert_topic/',insert_topic,name='insert_topic'),
    path('insert_webpage/',insert_webpage,name='insert_webpage'),
    path('insert_accessrecord/',insert_accessrecord,name='insert_accessrecord'),
    path('data_display/',data_display,name='data_display'),
    path('data_retriev/',data_retriev,name='data_retriev'),
    path('data_order/',data_order,name='data_order'),
    path('field_lookups/',field_lookups,name='field_lookups'),
    path('sel_rel_method/',sel_rel_method,name='sel_rel_method'),
    path('prerecth_rel_method/',prerecth_rel_method,name='prerecth_rel_method'),
    #path('aggregate_functions/',aggregate_functions,name='aggregate_functions'),
    path('dummy/',dummy,name='dummy'),
    path('home/',home,name='home'),
    path('alerts/',alerts,name='alerts'),
    path('buttons/',buttons,name='buttons'),
    path('forms/',forms,name='forms'),
    path('badge/',badge,name='badge'),
    path('dropdown/',dropdown,name='dropdown'),
    path('buttongroup/',buttongroup,name='buttongroup'),
]

