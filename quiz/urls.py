from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('<int:courseID>/<int:lessonID>/create-assignment', views.createAssignment, name = 'assignmentCreate'),
    path('<int:courseID>/<int:lessonID>/<int:assignmentID>', views.viewAssignment, name = 'viewAssignment'),


    path('create', views.createCourse, name='create'),
    path("<int:courseID>", views.viewCourse, name="viewCourse"),
    path('lesson', views.createLesson, name='lesson'),

]