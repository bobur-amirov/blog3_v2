from django.urls import path

from .views import *

urlpatterns = [
    path('', BlogList.as_view(), name='blog_list'),
    path('blog/<slug:slug>', BlogDetail.as_view(), name='blog_detail'),
    path('category/<slug:slug>', BlogByCategory.as_view(), name='category_blogs'),
    path('create', BlogCreate.as_view(), name='blog_create'),
]
