from django.contrib import admin
from .models import blogpost,postcomment
# Register your models here.

admin.site.register(blogpost)

admin.site.register(postcomment)