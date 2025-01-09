from django.db import models
# from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=255,null=True)
    description = CKEditor5Field(config_name='default')
    blog_image=models.ImageField(upload_to="blog_image",verbose_name="blog_main_image")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title