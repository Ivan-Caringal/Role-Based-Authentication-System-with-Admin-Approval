from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns= [
path("", views.landing, name="landing"),
path("home/", views.index, name="index"),
path('login/', LoginView.as_view(template_name='register/templates/BarangayLogin.html'), name='login'),
]