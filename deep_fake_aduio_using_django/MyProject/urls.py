"""
URL configuration for MyProject project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from MyApp import views
urlpatterns = [
    path('admin', admin.site.urls),
    path('upload/',views.index,name="upload"),
    path('', views.home ,name="home"),
    path('signup',views.signup, name='signup'),
    path('logout/',views.logout,name="logout"),
    path("index/", views.index1, name='index'),
    path('about/',views.about, name = 'about'),
 
    path('contact/', views.contact, name='contact'),

    path('signup_data_to_db', views.signup_data_to_db, name="signup_data_to_db"),
    path('login_data_to_db', views.login_data_to_db, name="login_data_to_db"),
    path('output/',views.output, name =  'output'),
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
