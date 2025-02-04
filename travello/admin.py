from django.contrib import admin
from .models import Destination, Comments, VisitorTracking

# Register your models here.
admin.site.register(Destination)
admin.site.register(Comments)
admin.site.register(VisitorTracking)