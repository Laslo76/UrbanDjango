"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from task2.views import task2_func, task2
from task3.views import MainPage, Basket, Shop

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task2/', task2_func),
    path('class_task/', task2.as_view()),
    path('fisher/', MainPage.as_view()),
    path('shop/', Shop.as_view()),
    path('basket/', Basket.as_view())

]
