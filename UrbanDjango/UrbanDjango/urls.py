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
from task3.views import MainPage as Mainpage3
from task3.views import Basket as Basket3
from task3.views import Shop as Shop3
from task4.views import MainPage, Basket, Shop
from task5.views import sign_up_by_html, sign_up_by_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task2/', task2_func),
    path('class_task/', task2.as_view()),
    path('fisher/', Mainpage3.as_view()),
    path('shop/', Shop3.as_view()),
    path('basket/', Basket3.as_view()),
    path('week/', MainPage.as_view()),
    path('shop_week/', Shop.as_view()),
    path('basket_week/', Basket.as_view()),
    path('', sign_up_by_html),
    path('reg/', sign_up_by_django)

]
