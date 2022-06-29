
from django.urls import path

from . import views # . here is used for same file
app_name='blog'

urlpatterns = [
    
    path('hello',views.all_blogs,name='blog/all_blogs'),
    path('<int:blog_id>/',views.detail,name='blog/detail'),
   
    
]  