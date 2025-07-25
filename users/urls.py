from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import valid_user_from_email, CustomUserCreationView

app_name = 'users'
urlpatterns = [
    path("registration/", CustomUserCreationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('valid_token/<str:token>', valid_user_from_email, name='valid_token'),
]