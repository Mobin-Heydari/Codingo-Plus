from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, CustomerViewSet


app_name = "Profiles"



urlpatterns = [
    
]


router = DefaultRouter()

router.register(r'employees', EmployeeViewSet, basename="employees")

router.register(r'customers', CustomerViewSet, basename="customers")

urlpatterns = router.urls