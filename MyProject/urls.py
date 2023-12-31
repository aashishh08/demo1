"""
URL configuration for MyProject project.

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
from django.urls import path
from MyProject import views

urlpatterns = [
    path('admin/', admin.site.urls, name = "admin"),
    path('about-us/', views.aboutUs, name = "aboutus"),
    # path('course/', views.aboutUs),
    # int: can be int, str, slug(course-details)
    path('course/<int:courseid>', views.course, name="course"),
    path('', views.HomePage, name="home"),
    path('user-form/', views.userForm, name="form"),
    path('submit-form/', views.submitForm, name="submit-form"),
    path('calculator/', views.calculator, name="calculator"),
    path('checkEvenOdd/', views.check, name="check"),
    path('service-page/', views.service, name="service")

]
