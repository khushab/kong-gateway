from django.urls import path
from . import views

urlpatterns = [
  path('', views.hello_world, name='hello_world'),
  path('<str:file_path>/', views.simulate_cdn_upload, name='simulate_cdn_upload'),
]