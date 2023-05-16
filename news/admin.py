from django.contrib import admin
from . models import*

# Register your models here.
@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display=['id', 'name', 'slug']
    preoccupied_fields={'slug':('name',)}


admin.site.register(News)

admin.site.register(pages)