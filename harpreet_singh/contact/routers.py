from rest_framework.routers import DefaultRouter

from contact.views import ContactViewSet
from Blog.views import BlogViewSet
from Pdf_management.views import PdfManagementViewset
router=DefaultRouter()

router.register("contact",ContactViewSet,basename="contact")
router.register("blog",BlogViewSet,basename="blog")
router.register("PdfManagemnt",PdfManagementViewset,basename="PdfManagemnt")



