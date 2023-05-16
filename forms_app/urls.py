"""
URL configuration for forms_app project.

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
from django.contrib.auth.views import LoginView
from myForms.views import home,Check,register_request,login_request,logout_request, pioneer_home,message_view,about_us,contact_us,hazard


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',pioneer_home,name="pioneer_home"),
    path('home/', home,name='home'),
    path('hazard/', hazard, name='hazard'),
    path('checkin/',Check,name='checkin'),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name= "logout"),
    path("message_view/",message_view,name="message_view"),
    path('about/', about_us,name='about_us'),
    path('contact/',contact_us,name='contact_us'),
    path('login/', LoginView.as_view(), name='login'),
    # path('login/', )
    #path("pioneer", pioneer_home, name= "pioneer_home"),

    # path('positive/', positive.html)
    #path('login/', login),
    #path('register', signup),
]
