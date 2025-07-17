import os 
from django.db.models.signals import post_save

from django.dispatch import receiver
from .models import PropertyValuationFile, PropertyValuationModel
import pandas as pd
from django.conf import settings

@receiver(post_save, sender=PropertyValuationFile)
def import_property_valuation(sender, instance, created, **kwargs):
    
        # Delete old files (keep only the current one)
        old_files = PropertyValuationFile.objects.exclude(id=instance.id)
        for old_file in old_files:
            if old_file.file:
                try:
                    os.remove(old_file.file.path)
                except Exception as e:
                    print("Error deleting old file:", e)
            old_file.delete()

        # Delete old valuation data
        PropertyValuationModel.objects.all().delete()

        # Load the Excel file
        file_path = instance.file.path
        df = pd.read_excel(file_path)

        # Expecting columns: City, Apartment Price, House Price, Plot Price
        for _, row in df.iterrows():
            PropertyValuationModel.objects.create(
                city=row["City"],
                apartment_price_per_meter_square=row["Apartment_Price_Meter_Square"],
                house_price_per_meter_square=row["House_Price_Meter_Square"],
                plot_price_per_meter_square=row["Plot_Price_Meter_Square"]
            )