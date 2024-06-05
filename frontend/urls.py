from django.urls import path
from .views import index, ask

urlpatterns = [
    path('', index, name="Home"),
    path('ask/', ask, name="Ask"),
]
