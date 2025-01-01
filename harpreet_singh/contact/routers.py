from rest_framework.routers import DefaultRouter

from contact.views import ContactViewSet
router=DefaultRouter()

router.register("contact",ContactViewSet,basename="contact")

