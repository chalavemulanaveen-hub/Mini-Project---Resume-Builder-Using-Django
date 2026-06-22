from django.urls import path
from . import views

urlpatterns = [

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'home/',
        views.home,
        name='home'
    ),

    path(
        'form/',
        views.resume_form,
        name='form'
    ),

    path(
        'my-resumes/',
        views.my_resumes,
        name='my_resumes'
    ),

    path(
        'view/<int:id>/',
        views.view_resume,
        name='view_resume'
    ),

    path(
        'delete/<int:id>/',
        views.delete_resume,
        name='delete_resume'
    ),
]