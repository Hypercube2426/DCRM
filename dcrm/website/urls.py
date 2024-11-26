from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home , name = 'home'),
    path('login/', views.login_user , name = 'login'),
    path('logout/', views.logout_user , name = 'logout'),

]
#webpage is a 3 step process ->
# create template file , html , url , view
