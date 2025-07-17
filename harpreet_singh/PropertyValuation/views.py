from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from PropertyValuation.models import PropertyValuationModel
from PropertyValuation.serializer import PropertyValuationSerializer

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import PropertyValuationModel
import threading


class PropertyValuationViewset(ModelViewSet):
    queryset = PropertyValuationModel.objects.all()
    serializer_class = PropertyValuationSerializer

    @action(detail=False, methods=["POST"], url_path="get-result")
    def get_result(self, request, *args, **kwargs):
        street_address = request.data.get("street_address")
        house_number = request.data.get("house_number")
        email = request.data.get("email")
        m2 = request.data.get("property_size")
        city = request.data.get("city_name")
        property_type = request.data.get("property_type")

        print(m2, city, property_type)
        if not m2 or not city or not property_type:
            return Response(
                {"success": False, "message": "Please provide all fields."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            m2 = float(m2)
        except:
            return Response(
                {"success": False, "message": "Property size must be a number."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        city_price_instance = PropertyValuationModel.objects.filter(city=city).first()
        if not city_price_instance:
            return Response(
                {"success": False, "message": "City is not available"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Determine price per m²
        if property_type == "House":
            value = float(city_price_instance.house_price_per_meter_square)
        elif property_type == "Apartment":
            value = float(city_price_instance.apartment_price_per_meter_square)
        elif property_type == "Plot":
            value = float(city_price_instance.plot_price_per_meter_square)
        else:
            return Response(
                {"success": False, "message": "Invalid property type"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        estimated_price = round(m2 * value)
        price_min = estimated_price - 2000
        price_max = estimated_price + 2000

        # Email context
        context = {
            "logo_url": "https://www.ghotra-immobilien.com/static/images/website logo updated.png",  # Replace with your actual logo URL
            "property_type": property_type,
            "city": city,
            "address": f"{street_address}, {house_number}",
            "size": m2,
            "estimated_price": f"{estimated_price:,} €",
            "range_min": f"{price_min:,} €",
            "range_max": f"{price_max:,} €",
        }

        # Render email
        html_message = render_to_string("property_estimate.html", context)
        plain_message = strip_tags(html_message)

        # Send email

        threading.Thread(
            target=send_mail,
            kwargs={
                "subject": "🏡 Your Property Valuation Estimate",
                "message": plain_message,
                "from_email": "kartikprajapati26122004@gmail.com",
                "recipient_list": [email],
                "html_message": html_message,
            },
        ).start()
        
        return Response(
            {
                "success": True,
                "message": f"Estimated price: {estimated_price} €. Email sent to {email}.",
            },
            status=status.HTTP_200_OK,
        )

    @action(detail=False, methods=["GET"], url_path="city-name")
    def city_name(self, request, *args, **kwargs):

        cities = (
            PropertyValuationModel.objects.order_by("id")
            .values_list("city", flat=True)
            .distinct()
        )
        return Response(
            {"success": True, "data": list(cities)}, status=status.HTTP_200_OK
        )
