from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('tarif/', views.TarifView, name='tarif'),
    path('add-course/', views.CreateCourseView.as_view(), name='add_course'),
    path('course/<slug>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('course/<slug>/<lessons_slug>', views.LessonDetailView.as_view(), name='lesson_detail'),
]