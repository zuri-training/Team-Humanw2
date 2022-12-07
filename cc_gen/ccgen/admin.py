from django.contrib import admin

# Register your models here.
from .models import Download, Design, Comment

admin.site.register(Download)
admin.site.register(Design)
admin.site.register(Comment)
