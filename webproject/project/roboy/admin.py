from django.contrib import admin

# Register your models h
from .models import user_details,user_images

admin.site.register(user_details)
admin.site.register(user_images)

