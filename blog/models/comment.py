from django.db import models

from account.models import Account
from .blog import Blog

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()

    def __str__(self):
        return self.text