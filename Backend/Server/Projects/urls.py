from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views


app_name = "Projects"


urlpatterns = [
    
]

router = DefaultRouter()

router.register(r'', views.ProfileViewset, basename="projects")

urlpatterns += router.urls
