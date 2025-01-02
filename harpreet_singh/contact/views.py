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
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
    def create(self, request, *args, **kwargs):
        required_fields = [
            ('username', 'Benutzername ist erforderlich'),
            ('email', 'E-Mail ist erforderlich'),
            ('phone', 'Telefonnummer ist erforderlich'),
            ('message', 'Nachricht ist erforderlich')
        ]

        for field, error_message in required_fields:
            value = request.data.get(field)
            if not value:
                return Response({"success": False, "message": error_message}, status=status.HTTP_400_BAD_REQUEST)

        username = request.data.get("username")
        email = request.data.get("email")
        phone = request.data.get("phone")
        message = request.data.get("message")

        # E-Mail-Validierung
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            return Response({"success": False, "message": "Ungültiges E-Mail-Format"}, status=status.HTTP_400_BAD_REQUEST)

        # Telefonvalidierung (angenommen 10 Ziffern für dieses Beispiel)
        if not phone.isdigit():
            return Response({"success": False, "message": "Ungültige Telefonnummer"}, status=status.HTTP_400_BAD_REQUEST)

        # Nachrichtenlängen-Validierung
        if len(message) < 20 or len(message) > 200:
            return Response({"success": False, "message": "Die Nachricht sollte zwischen 20 und 200 Zeichen lang sein"}, status=status.HTTP_400_BAD_REQUEST)

        subject = "Neue Anfrage von der Website"
        recipient_email = "info@ghotra-immobilien.com"
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
        
        return Response({"success": True, "message": "Nachricht an den Eigentümer wurde erfolgreich gesendet. Er wird sich so schnell wie möglich bei Ihnen melden."}, status=status.HTTP_200_OK)
