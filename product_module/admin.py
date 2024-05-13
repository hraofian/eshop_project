from django.contrib import admin

from . import models

class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug']
    prepopulated_fields={
        'slug':['title']
    }

    list_display = ['__str__' , 'title' , 'price' , 'is_active']
    list_filter = ['price' , 'is_active']
    list_editable = ['title' , 'is_active' , 'price']

admin.site.register(models.Product , ProductAdmin)