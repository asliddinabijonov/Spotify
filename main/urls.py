from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from mainApp.views import *

from rest_framework.routers import DefaultRouter

schema_view = get_schema_view(
    openapi.Info(
        title="Omborxona API",
        default_version='v1',
        description="Test description",
        terms_of_service="#",
        contact=openapi.Contact(email="https://asliddinabijonov04@gmail.com"),
        license=openapi.License(name="#"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('qoshiqchilar/', QoshiqchiListCreateAPIView.as_view()),
    path('qoshiqchilar/<int:pk>/', QoshiqchiRetrieveUpdateDestroyAPIView.as_view()),

    path('albomlar/', AlbomListCreateAPIView.as_view()),
    path('albomlar/<int:pk>/', AlbomRetrieveUpdateDestroyAPIView.as_view()),

    path('qoshiqlar/', QoshiqListCreateAPIView.as_view()),
    path('qoshiqlar/<int:pk>/', QoshiqRetrieveUpdateDestroyAPIView.as_view()),

    path('', schema_view.with_ui('swagger', cache_timeout=0)),
]
