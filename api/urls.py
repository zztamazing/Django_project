from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # simplejwt
    # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.getRoutes),
    path('projects/', views.getProjects),
    path('project/<str:pk>', views.getProject),

]
