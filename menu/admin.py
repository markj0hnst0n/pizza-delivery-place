from django.contrib import admin
from .models import MenuItem, Category, Allergens


class AllergenInline(admin.TabularInline):
    model = MenuItem.allergens.through


class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
        'vegetarian',
        'spicy',
    )

    exclude = ('allergens',)

    inlines = [
        AllergenInline,
    ]

    ordering = ('name',)


admin.site.register(MenuItem, MenuAdmin)
admin.site.register(Category)
admin.site.register(Allergens)
