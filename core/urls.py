from django.urls import path
from django.http import HttpResponse
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',views.ListTask.as_view(),name='list-task'),
    path('task/<str:pk>/',views.TaskDetail.as_view(),name='details'),
    path('create/',views.CreateTask.as_view(),name='create'),
    path('update-task/<str:pk>/',views.UpdateTask.as_view(),name='update-task'),
    path('login/',views.UserLoginView.as_view(),name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('signup/',views.CreataUserView.as_view(),name='signup'),
    path('delete/<str:pk>',views.DeleteTask.as_view(),name="delete")
]
