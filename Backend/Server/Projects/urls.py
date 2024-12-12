from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


app_name = "Projects"



router = DefaultRouter()

router.register(r'projects', views.ProjectViewSet, basename="projects")
router.register(r'categories', views.CategoryViewSet, basename="category")

urlpatterns = [
   path('', include(router.urls))
]