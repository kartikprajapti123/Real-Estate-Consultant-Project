from rest_framework.routers import DefaultRouter

from contact.views import ContactViewSet
from Blog.views import BlogViewSet
from Pdf_management.views import PdfManagementViewset
from PropertyValuation.views import PropertyValuationViewset

router=DefaultRouter()

router.register("contact",ContactViewSet,basename="contact")
router.register("blog",BlogViewSet,basename="blog")
router.register("PdfManagemnt",PdfManagementViewset,basename="PdfManagemnt")
router.register("apiproperty",PropertyValuationViewset,basename="PropertyValuation")






