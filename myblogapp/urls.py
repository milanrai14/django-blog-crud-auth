from django.urls import path
from .views import register, login, logout, bloglist, delete, update

urlpatterns = [
    path('bloglist/', bloglist, name= "bloglist"),
    path('', register, name='register'),
    path('login/', login, name= "login"),
    path('logout/', logout, name = "logout"),
    path('delete/<int:id>', delete, name="delete"),
    path('update/<int:id>', update, name= "update")
    
]
