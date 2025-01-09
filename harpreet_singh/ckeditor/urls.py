from django.urls import path
from ckeditor.views import ckeditor_upload

urlpatterns = [
    path('upload/', ckeditor_upload, name='ckeditor-upload'),
]
