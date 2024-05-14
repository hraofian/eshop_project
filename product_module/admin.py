from django.contrib import admin

from . import models

class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug']
    prepopulated_fields={
        'slug':['title']
    }

    list_display = ['__str__' , 'title' , 'price' , 'is_active', 'category']
    list_filter = ['price' , 'is_active']
    list_editable = ['title' , 'is_active' , 'price']

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display=['__str__' ,'title' , 'url_title']

admin.site.register(models.Product , ProductAdmin)

admin.site.register(models.ProductCategory , ProductCategoryAdmin)
admin.site.register(models.ProductInformation)
admin.site.register(models.ProductTag)