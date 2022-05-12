from django.db import models

from account.models import Account

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(upload_to='category/')
    description = models.TextField()
    user = models.ManyToManyField(Account, related_name='category', null=True, blank=True)

    def __str__(self):
        return self.name