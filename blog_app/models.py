from django.db import models
from tinymce import models as tinymce_models

# Create your models here.

class blogpost(models.Model):
    title=models.CharField(max_length=220)
    subtitle=models.CharField(max_length=220)
    blog_image=models.ImageField(upload_to='post_image')
    content=tinymce_models.HTMLField()
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class postcomment(models.Model):
    post= models.ForeignKey(blogpost,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_author=models.CharField(max_length=120)
    created_comment_date=models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.comment_author
