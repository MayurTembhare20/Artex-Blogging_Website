# Generated by Django 4.1.3 on 2023-02-25 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_alter_blogpost_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='postcomment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.TextField()),
                ('comment_author', models.CharField(max_length=120)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_app.blogpost')),
            ],
        ),
    ]
