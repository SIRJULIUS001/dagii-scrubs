
from django.contrib import admin
from .models import GalleryImage, ContactMessage
from .models import BlogPost

admin.site.register(GalleryImage)
admin.site.register(ContactMessage)
admin.site.register(BlogPost)

# Register your models here.
