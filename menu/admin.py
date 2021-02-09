from django.contrib import admin
from .models import MenuItem, Category

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
        'allergens',
        'spicy',
        'vegetarian',
    )

    ordering = ('name',)

admin.site.register(MenuItem, MenuAdmin)
admin.site.register(Category)
