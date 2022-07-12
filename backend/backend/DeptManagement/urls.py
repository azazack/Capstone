from .views import Register, Login,UserView,Logout
from django.urls import path

urlpatterns = [
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    path('me', UserView.as_view()),
    path('logout', Logout.as_view())
]
