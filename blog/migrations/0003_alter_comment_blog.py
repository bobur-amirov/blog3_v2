# Generated by Django 4.0.4 on 2022-04-26 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='blog.blog'),
        ),
    ]
