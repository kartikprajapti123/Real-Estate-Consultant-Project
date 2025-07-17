from django.db import models

# Create your models here.
class PropertyValuationModel(models.Model):
    
    city=models.CharField(max_length=20,null=True,blank=True)
    apartment_price_per_meter_square=models.CharField(max_length=10,null=True,blank=True)
    house_price_per_meter_square=models.CharField(max_length=10,null=True,blank=True)
    plot_price_per_meter_square=models.CharField(max_length=10,null=True,blank=True)
    
    
    
    def __str__(self):
        return self.city
    
    class  Meta:
        verbose_name = 'Property_valuation'
        verbose_name_plural = 'Property_valuation'
    
    
    
class PropertyValuationFile(models.Model):
    
    file=models.FileField(upload_to="PropertyValuationFile")
    
    
    
    def __str__(self):
        return "City Price File"
    
    class  Meta:
        verbose_name = 'City Prices Files'
        verbose_name_plural = 'City Prices Files'
    