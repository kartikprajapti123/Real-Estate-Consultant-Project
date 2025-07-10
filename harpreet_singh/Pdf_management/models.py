from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
class PdfManagement(models.Model):
    pdf_name=models.CharField(max_length=255,blank=True,null=True)
    
    pdf_file = models.FileField(
        upload_to="pdf/",
        blank=False,
        null=False,
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )
    
    def __str__(self):
        return str(self.pdf_file)
    
    
    # class meta:
        # verbose_name="File Management"
        # verbose_name_plural="File Management"
        