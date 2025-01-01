from rest_framework import serializers
from contact.models import Contact
class ContactSerializer(serializers.ModelSerializer):
    model=Contact
    fields=[
        "username",
        "email",
        "phone_number",
        "message"
    ]
    
    