from django.urls import path

from .views import *

urlpatterns = [
    path('', BlogList.as_view(), name='blog_list'),
    path('blog/<slug:slug>', BlogDetail.as_view(), name='blog_detail'),
    path('category/<slug:slug>', BlogByCategory.as_view(), name='category_blogs'),
    path('tag/<slug:slug>', BlogByTag.as_view(), name='tag_blogs'),
    path('create', BlogCreate.as_view(), name='blog_create'),
    path('comment-delete/<int:pk>', CommentDelete.as_view(), name='comment_delete'),
]
