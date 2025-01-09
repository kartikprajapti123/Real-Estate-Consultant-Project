from rest_framework.routers import DefaultRouter

from contact.views import ContactViewSet
from Blog.views import BlogViewSet
router=DefaultRouter()

router.register("contact",ContactViewSet,basename="contact")
router.register("blog",BlogViewSet,basename="blog")


