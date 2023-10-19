from django.urls import path
from . import views

urlpatterns = [
    path('teacher', views.teacherView, name='teacher'),
    path('student', views.studentView, name='student'),
    path('', views.generate_certificate, name='generate_certificate'),
    path('verify_certificate/<int:id>/', views.verify_certificate, name='verify-certificate'),

]
