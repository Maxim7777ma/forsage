"""
URL configuration for forsage_school project.

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
from django.urls import path, include
<<<<<<< HEAD
from courses import views  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.about, name='about'), 
    path('course_list/', views.course_list, name='course_list'), 
=======
from courses import views  # Импортируем views из вашего приложения

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.about, name='about'),  # Маршрут для страницы about как корневой
    path('course_list/', views.course_list, name='course_list'),  # Маршрут для страницы курсов
>>>>>>> 79c4817e39626633e9d58ce9a1eb13dec6e8c871
]