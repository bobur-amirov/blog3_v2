from django.contrib import admin

from .models import Category, Blog, Tag, Comment

admin.site.register([Category, Blog, Tag, Comment])
