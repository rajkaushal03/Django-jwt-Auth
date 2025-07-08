from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('verify/', views.VerifyTokenView.as_view(), name='verify'),
    path('validate/', views.ValidateTokenView.as_view(), name='validate'),
]
