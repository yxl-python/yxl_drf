from django.urls import path
from app import views

urlpatterns = [
    path("register/",views.RegisterViewSetView.as_view({"post":"user_register"})),
    path("register/<str:id>/",views.RegisterViewSetView.as_view({"post":"user_register"})),

    path("login/",views.LoginViewSetView.as_view({"post":"user_login",})),
    path("login/<str:id>/",views.LoginViewSetView.as_view({"post":"user_login"})),
]