
from django.contrib import admin
from django.urls import path, include
from app.views import *
urlpatterns = [
   
    path('', hello, name='hello'),
    path('posts', all_posts, name='all_posts'),
    path('post/update/<int:id>', post_update, name='post_update'),
    path('post/delete/<int:id>', post_delete, name='post_delete'),
    
]
