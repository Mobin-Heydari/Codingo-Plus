from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.routers import DefaultRouter

# Create an instance of your custom router
router = DefaultRouter()

# Register the BlogViewSet with the custom router
# This will automatically create the standard CRUD routes for the BlogViewSet
router.register(r'', views.BlogViewSet, basename='blog')

# Define the URL patterns using your custom router
urlpatterns = [
    # Include all the URLs generated by the custom router
    # This will include both the default routes and any custom routes defined in the router
    path('blog/', include(router.urls)),
    path('categories/', views.CategoryListAPIView.as_view(), name="category_list"),
    path('category/<slug:slug>/', views.CategoryDetailAPIView.as_view(), name="category_list"),
]