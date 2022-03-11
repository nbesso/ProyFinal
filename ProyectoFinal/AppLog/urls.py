from django.urls import path
from .views import login_request, register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('cuenta/login/', login_request, name='login'),
    path('cuenta/logout/', LogoutView.as_view(template_name='AppLog/logout.html'), name='logout'),
    path('cuenta/register/', register, name='Register'),
    ]