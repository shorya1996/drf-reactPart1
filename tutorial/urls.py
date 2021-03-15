from django.contrib import admin
from django.urls import path
from api import views
# from rest_framework_swagger.views import get_swagger_view
# schema_view = get_swagger_view(title='My swagger')
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="DRF Tutorial  API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('signupapi/', views.SignupAPI.as_view()),
    path('loginapi/', views.LoginApi.as_view()),
    path('userdetails/', views.UserDetails.as_view()),
    path('userdetails/<int:pk>/', views.UserDetails.as_view()),
]
