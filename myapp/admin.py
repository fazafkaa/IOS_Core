from django.contrib import admin
from .models import Folder, File, Profile

admin.site.register(Folder)
admin.site.register(File)
admin.site.register(Profile)