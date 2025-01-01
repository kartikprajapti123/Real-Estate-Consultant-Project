from django.urls import path
from render import views
urlpatterns=[
    path("",views.home,name="home"),
    path("about-us/",views.about_us,name="about-us"),
    path("service/",views.service,name="service"),
    path("contact/",views.contact,name="contact")
    
]