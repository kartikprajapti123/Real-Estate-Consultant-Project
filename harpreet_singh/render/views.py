from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"index.html")

def service(request):
    return render(request,"service.html")

def contact(request):
    return render(request,"contact.html")

def about_us(request):
    return render(request,"about.html")


def data_protection(request):
    return render(request,"data_protection.html")
    
    

def imprint(request):
    return render(request,"imprint.html")
    


def blog(request):
    return render(request,"blog.html")
    
    
def blog_detail(request,blog_name):
    return render(request,"blog_detail.html")
    
def not_found(request, exception):
    return render(request, '404_not_found.html', status=404)    



# //////////////////////////english////////////////////////////////////////////




def en_home(request):
    return render(request,"index-en.html")

def en_service(request):
    return render(request,"service-en.html")

def en_contact(request):
    return render(request,"contact-en.html")

def en_about_us(request):
    return render(request,"about-en.html")


def en_data_protection(request):
    return render(request,"data_protection-en.html")
    
    

def en_imprint(request):
    return render(request,"imprint-en.html")
    


def en_blog(request):
    return render(request,"blog-en.html")
    
    
def en_blog_detail(request,blog_name):
    return render(request,"blog-detail-en.html")


# ///////////////////////////english end //////////////////////////

def chi_home(request):
    return render(request,"index-chi.html")

def chi_service(request):
    return render(request,"service-chi.html")

def chi_contact(request):
    return render(request,"contact-chi.html")

def chi_about_us(request):
    return render(request,"about-chi.html")


def chi_data_protection(request):
    return render(request,"data_protection-chi.html")
    
    

def chi_imprint(request):
    return render(request,"imprint-chi.html")
    


def chi_blog(request):
    return render(request,"blog-chi.html")
    
    
def chi_blog_detail(request,blog_name):
    return render(request,"blog-detail-chi.html")