from django.urls import path
from .views import AccountRegistration, user_login, logout, index

urlpatterns = [
    path('signup/', AccountRegistration.as_view(), name = 'signup'),
    path('', user_login, name = 'login'),
    path('logout/', logout, name = 'logout'),
    path('index/', index, name = 'index'),

    ]