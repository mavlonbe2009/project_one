from django.urls import path
from .views import *
from account.views import * 
urlpatterns = [
    path("",Malumot,name="store_panel"),
    path("<slug:category_slug>/",Malumot,name="category_by_slug"),
    path("view_detail/<int:id>/", Detail, name="detail_name"),
    path("", user_login,name="login")
    
    
    
]
