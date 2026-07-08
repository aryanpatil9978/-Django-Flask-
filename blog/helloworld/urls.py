from . import views
from django.urls import path

urlpatterns = [
    path("/helloworld",views.HelloWorldView.as_view())
]

