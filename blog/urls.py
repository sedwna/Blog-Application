from django.urls import path
from . import views, admin

app_name = 'blog'

urlpatterns = [
    path('',views.index,name='index'),
    path('posts/',views.post_list,name='post_detail'),
    path('posts/<int:pk>/',views.post_detail,name='post_detail'),
]
