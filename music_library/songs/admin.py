from django.contrib import admin
from .models import Song
from .serializers import SongSerializer
from rest_framework.response import Response

# Register your models here.
admin.site.register(Song)

