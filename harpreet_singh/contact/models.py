from django.db import models

# Create your models here.
class Contact(models.Model):
    username=models.CharField(max_length=255,null=True)
    email=models.CharField(max_length=255,null=True)
    phone_number=models.CharField(max_length=255,null=True)
    message=models.TextField(max_length=255,null=True)
    
    def __str__(self):
        return self.username