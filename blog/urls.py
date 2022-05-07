from django.urls import path

from .views import *

urlpatterns = [
    path('', BlogList.as_view(), name='blog_list'),
    path('blog/<slug:slug>', BlogDetail.as_view(), name='blog_detail'),
    path('category/<slug:slug>', BlogByCategory.as_view(), name='category_blogs'),
    path('tag/<slug:slug>', BlogByTag.as_view(), name='tag_blogs'),
    path('create/', BlogCreate.as_view(), name='blog_create'),
    path('comment-delete/<int:pk>', CommentDelete.as_view(), name='comment_delete'),
    path('blog-update/<slug:slug>', BlogUpdate.as_view(), name='blog_update'),
    path('blog-delete/<slug:slug>', BlogDelete.as_view(), name='blog_delete'),
    path('category-list', CategoryList.as_view(), name='category_list'),
    path('category-user/<slug:slug>', CategoryAddUser.as_view(), name='category_user_add'),
]
