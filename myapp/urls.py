from django.urls import path, include
from myapp.views import Typing_speed
urlpatterns = [
    path('test/',Typing_speed , name="test")
]
