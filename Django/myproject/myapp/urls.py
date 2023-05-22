from django.urls import path
from myapp.views import hello_world
from .views import RunPlaybookView

urlpatterns = [
    path('hello/', hello_world),
    path('run-playbook/', RunPlaybookView.as_view()),
]