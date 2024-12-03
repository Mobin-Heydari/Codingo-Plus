from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


app_name = "Contact-Us"  # Namespace for the URL patterns in this app


# Define the URL patterns for this app
urlpatterns = [
    # This list will be populated with URL patterns later
]


# Create an instance of DefaultRouter
router = DefaultRouter()

# Register the ContactViewSet with the router
# This will automatically create the necessary routes for CRUD operations
router.register(r'', views.ContactViewSet, basename='contactus')

# Extend the urlpatterns with the router's URLs
urlpatterns += router.urls