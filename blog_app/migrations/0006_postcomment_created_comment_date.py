# Generated by Django 4.1.3 on 2023-07-13 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_postcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='created_comment_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
