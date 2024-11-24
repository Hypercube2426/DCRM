from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home , name = 'home'),

]
#webpage is a 3 step process ->
# create template file , html , url , view
