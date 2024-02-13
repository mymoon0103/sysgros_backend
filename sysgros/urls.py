

from django.urls import path
from  .views import RegisterView, LoginView, UserProfileView, LogOutView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('profile', UserProfileView.as_view()),
    path('logout', LogOutView.as_view()),
]
