from django.urls import path
from . import views

<<<<<<< HEAD

urlpatterns = [
    path('', views.about, name='about'),
=======
urlpatterns = [
    path('', views.about, name='about'),  # Пустой путь для корневой страницы
>>>>>>> 79c4817e39626633e9d58ce9a1eb13dec6e8c871
    path('course_list/', views.course_list, name='course_list'),
]