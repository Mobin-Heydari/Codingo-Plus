from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeProfileViewSet, SimpleUserProfileViewSet


app_name = "Profiles"



urlpatterns = [
    
]


router = DefaultRouter()

router.register(r'employees', EmployeeProfileViewSet, basename="employees")

router.register(r'simple-user', SimpleUserProfileViewSet, basename="simple-user")

urlpatterns = router.urls