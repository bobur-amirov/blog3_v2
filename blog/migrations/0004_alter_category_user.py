# Generated by Django 4.0.4 on 2022-05-10 10:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_alter_comment_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='user',
            field=models.ManyToManyField(blank=True, null=True, related_name='category', to=settings.AUTH_USER_MODEL),
        ),
    ]