
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('services',views.services,name='services'),
    path('about',views.about,name='about'),
    path('create_record',views.create_record,name='create_record'),
    path('insert_service',views.insert_service,name='insert_service'),
    path('insert_service_record',views.insert_service_record,name='insert_service_record'),
    path('blog',views.blog,name='blog'),
    path('create_blog',views.create_blog,name='create_blog'),
    path('create_blog_record',views.create_blog_record,name='create_blog_record'),
    
]
