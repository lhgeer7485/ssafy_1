from django.urls import path
from . import views

app_name= 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('change_pw/', views.change_pw, name='change_pw'),
    path('delete/', views.delete, name='delete'),
]
