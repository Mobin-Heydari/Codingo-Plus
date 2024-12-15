from django.urls import path

from . import views


app_name ="FAQs"


urlpatterns = [
    path('', views.FaqAPIView.as_view(), name="FAQ_list")
]
