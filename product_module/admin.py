from django.contrib import admin

from . import models

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']

admin.site.register(models.Product , ProductAdmin)