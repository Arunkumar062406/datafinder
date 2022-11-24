from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('about/', views.About, name="about"),
    # path('signup/', views.Signup, name="signup"),
    path('pricing/', views.Pricing, name="pricing"),
    path('signin/', views.Signin, name="signin"),

]