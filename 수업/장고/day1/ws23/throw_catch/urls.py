from django.urls import path
from throw_catch import views
app_name = "throw_catch"
urlpatterns = [
    path('first/', views.first, name="first"),
    path('second/', views.second, name="second"),
]
