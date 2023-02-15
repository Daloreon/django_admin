from django.urls import path
from .views import *
urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationView.as_view()),
    path('login/', LoginApiview.as_view()),
    path('logout/', LogoutAPIView.as_view())
]
