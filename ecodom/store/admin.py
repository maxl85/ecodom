from django.contrib import admin
from .models import Category, Product
from mptt.admin import DraggableMPTTAdmin
from django.utils.safestring import mark_safe


class CategoryAdmin(DraggableMPTTAdmin):
    prepopulated_fields = {"slug": ("name",)}

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    save_as = True
    # save_on_top = True
    list_display = ('name', 'category', 'price', 'is_available', 'created_date', 'modified_date')
    list_display_links = ('name',)
    search_fields = ('category',)
    list_filter = ('category',)
    readonly_fields = ('created_date', 'modified_date', 'get_image')
    fields = ('name', 'slug', 'category', 'description', 'price', 'images', 'get_image', 'is_available', 'created_date', 'modified_date')

    def get_image(self, obj):
        if obj.images:
            return mark_safe(f'<img src="{obj.images.url}" width="150">')
        return '-'
    
    get_image.short_description = 'Фото'
    

admin.site.register(
    Category, CategoryAdmin,
        list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)
admin.site.register(Product, ProductAdmin)
