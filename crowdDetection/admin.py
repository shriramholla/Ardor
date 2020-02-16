from django.contrib import admin
from .models import Session, MusicSession

# Register your models here.
admin.site.register(Session)
admin.site.register(MusicSession)