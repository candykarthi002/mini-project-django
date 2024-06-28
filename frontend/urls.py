from django.urls import path
from .views import index, ask, plot, login_user, logout_user

urlpatterns = [
    path('', index, name="Home"),
    path('ask/', ask, name="Ask"),
    path('plot/', plot, name="Plot"),
    path('login/', login_user, name="Login"),
    path('logout/', logout_user, name="Logout"),
]
