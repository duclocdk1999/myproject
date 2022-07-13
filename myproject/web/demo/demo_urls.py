# 3rd parties
from django.urls import include, path

# Project module
from myproject.web.demo import views


urlpatterns = [
    path('hello/', views.hello_world)
]