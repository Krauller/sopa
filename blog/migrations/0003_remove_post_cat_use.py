# Generated by Django 4.1.4 on 2023-01-04 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_cat_use'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cat_use',
        ),
    ]
