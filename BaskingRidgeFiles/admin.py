from django.contrib import admin

# Register your models here.
from BaskingRidgeFiles.models import gallery_image, menu_entry, news_entry
from adminsortable2.admin import SortableAdminMixin

@admin.register(gallery_image)
class GalleryImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('image_tag', 'image')
    readonly_fields = ('image_tag',)


@admin.register(menu_entry)
class MenuAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'menu_name', 'menu_type', 'menu_pdf',)
    list_editable = ('menu_name', 'menu_type', 'menu_pdf', )


admin.site.register(news_entry)