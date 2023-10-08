from django.urls import path
from . import views

#URL Config
urlpatterns = [
    path('', views.bar_chart),
    path('hello/', views.sample_text),
    path('hello_html/', views.sample_html)
]