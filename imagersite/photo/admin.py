from django.contrib import admin

from .models import Photos, Album

admin.register(Photos)
admin.site.register(Album)
