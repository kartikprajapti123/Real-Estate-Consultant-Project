from Pdf_management.models import PdfManagement
from rest_framework import serializers

class PdfManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model=PdfManagement
        fields=["id","pdf_file","pdf_name"]
        
    def create(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    
    