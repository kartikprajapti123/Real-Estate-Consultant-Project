from django.contrib import admin
from django.contrib.auth.models import Group, User

# Unregister User and Group
admin.site.unregister(User)
admin.site.unregister(Group)

from Pdf_management.models import PdfManagement

admin.site.register(PdfManagement)
admin.site.site_header = "Ghotra Immobilien Admin Panel"
admin.site.site_title = "Ghotra Immobilien Admin Portal"
admin.site.index_title = "Welcome to Ghotra Immobilien Admin Panel"
