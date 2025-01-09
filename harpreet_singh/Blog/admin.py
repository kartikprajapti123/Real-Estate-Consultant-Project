from django.contrib import admin
from Blog.models import Blog
from django.contrib.auth.models import Group,User
# Register your models here.


admin.site.register(Blog)
admin.site.unregister(Group)
admin.site.unregister(User)

