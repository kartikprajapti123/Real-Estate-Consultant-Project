from django.urls import path
from render import views
urlpatterns=[
    path("",views.home,name="home"),
    path("google45af308f4d012cc3.html",views.google45af308f4d012cc3,name="google45af308f4d012cc3.html"),
    
    path("about-us/",views.about_us,name="about-us"),
    path("service/",views.service,name="service"),
    path("contact/",views.contact,name="contact"),
    path("imprint/",views.imprint,name="imprint"),
    path("data_protection/",views.data_protection,name="data_proctection"),
    path("blog/",views.blog,name="blog"),
    path("blog-detail/<str:blog_name>/",views.blog_detail,name="blog_detail"),
    path("book-a-appointment/",views.book_a_appointment,name="book_a_appointment"),
    path("pdf/",views.pdf,name="pdf"),
    
    
    
    path("en/index/",views.en_home,name="en_home"),
    path("en/about-us/",views.en_about_us,name="en_about_us"),
    path("en/service/",views.en_service,name="en_service"),
    path("en/contact/",views.en_contact,name="en_contact"),
    path("en/imprint/",views.en_imprint,name="en_imprint"),
    path("en/data_protection/",views.en_data_protection,name="en_data_proctection"),
    path("en/blog/",views.en_blog,name="en_blog"),
    path("en/blog-detail/<str:blog_name>/",views.en_blog_detail,name="en_blog_detail"),
    path("en/book-a-appointment/",views.en_book_a_appointment,name="book_a_appointment"),
    path("en/pdf/",views.en_pdf,name="en_pdf"),
    
    
    
    path("chi/index/",views.chi_home,name="chi_home"),
    path("chi/about-us/",views.chi_about_us,name="chi_about_us"),
    path("chi/service/",views.chi_service,name="chi_service"),
    path("chi/contact/",views.chi_contact,name="chi_contact"),
    path("chi/imprint/",views.chi_imprint,name="chi_imprint"),
    path("chi/data_protection/",views.chi_data_protection,name="chi_data_proctection"),
    path("chi/blog/",views.chi_blog,name="chi_blog"),
    path("chi/blog-detail/<str:blog_name>/",views.chi_blog_detail,name="chi_blog_detail"),
    
    
    
]