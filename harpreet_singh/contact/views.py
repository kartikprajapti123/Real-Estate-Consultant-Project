from django.shortcuts import render
from contact.models import Contact
from contact.serializer import ContactSerializer
# Create your views here.
from rest_framework.viewsets import ModelViewSet
import threading


from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

def send_email_with_template(subject, recipient_email, template_name, context):
    html_message = render_to_string(template_name, context)
    
    try:
        send_mail(
            subject=subject,
            message='',  
            from_email=settings.DEFAULT_FROM_EMAIL,  
            recipient_list=[recipient_email],
            fail_silently=False,  
            html_message=html_message 
        )
        return True
    except Exception as e:
        # Log or handle the exception as needed
        print(f"Failed to send email: {e}")
        return False


class ContactViewSet(ModelViewSet):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer
    
    def create(self, request, *args, **kwargs):
        required_fields = [
            ('username', 'Username is required'),
            ('email', 'Email is required'),
            ('phone', 'Phone is required'),
            ('message', 'Message is required')
        ]

        for field, error_message in required_fields:
            value = request.data.get(field)
            if not value:
                return Response({"success": False, "message": error_message}, status=status.HTTP_400_BAD_REQUEST)

        username = request.data.get("username")
        email = request.data.get("email")
        phone = request.data.get("phone")
        message = request.data.get("message")

        # Email validation
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            return Response({"success": False, "message": "Invalid email format"}, status=status.HTTP_400_BAD_REQUEST)

        # Phone validation (assuming 10 digits for example)
        if not phone.isdigit():
            return Response({"success": False, "message": "Invalid phone number"}, status=status.HTTP_400_BAD_REQUEST)

        # Message length validation
        if len(message) < 20 or len(message) > 200:
            return Response({"success": False, "message": "Message length should be between 20 and 200 characters"}, status=status.HTTP_400_BAD_REQUEST)

        subject = "New Inquiry from Website"
        recipient_email = "kartikprajapati26122004@gmail.com"
        template_name = "send_message.html"
        context = {
            "username": username,
            "email": email,
            "phone": phone,
            "message": message,
        }

        mail_thread = threading.Thread(
            target=send_email_with_template,
            args=(subject, recipient_email, template_name, context)
        )
        mail_thread.start()
        
        return Response({"success": True, "message": "Message to Owner has been send successfully, He will reach out to you as soon as possible"}, status=status.HTTP_200_OK)
