from django.urls import path
from .views import CostomLoginView

from django.contrib.auth.views import LogoutView 
from .views import RegisterPage



urlpatterns = [
    path('login/', CostomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

]
