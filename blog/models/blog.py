from ckeditor.fields import RichTextField
from django.db import models

from account.models import Account
from .category import Category
from .tag import Tag


class Blog(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ImageField(upload_to='blog/')
    description = RichTextField()
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='blog')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='blog')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
