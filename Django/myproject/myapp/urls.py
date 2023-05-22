from django.urls import path
from myapp.views import hello_world
from .views import RunPlaybookView
from . import views
from django.urls import path

urlpatterns = [
    path('hello/', hello_world),
    path('run-playbook/', RunPlaybookView.as_view()),
    path('stop/',views.stop_server, name='stop_server'),
]