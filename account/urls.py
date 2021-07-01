from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.AccountRegistration.as_view(), name = 'signup'),
    ]