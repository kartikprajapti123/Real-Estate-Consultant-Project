from django.urls import path
from render import views
urlpatterns=[
    path("",views.home,name="home"),
    path("about-us/",views.about_us,name="about-us"),
    path("service/",views.service,name="service"),
    path("contact/",views.contact,name="contact"),
    path("imprint/",views.imprint,name="imprint"),
    path("data_protection/",views.data_protection,name="data_proctection"),
    path("blog/",views.blog,name="blog"),
    path("blog-detail/<str:blog_name>/",views.blog_detail,name="blog_detail"),
    
    
    path("en/index/",views.en_home,name="en_home"),
    path("en/about-us/",views.en_about_us,name="en_about_us"),
    path("en/service/",views.en_service,name="en_service"),
    path("en/contact/",views.en_contact,name="en_contact"),
    path("en/imprint/",views.en_imprint,name="en_imprint"),
    path("en/data_protection/",views.en_data_protection,name="en_data_proctection"),
    path("en/blog/",views.en_blog,name="en_blog"),
    path("en/blog-detail/<str:blog_name>/",views.en_blog_detail,name="en_blog_detail"),
    
    
    
]