from django.contrib import admin
from shop.models import Item, ItemImage, Category, Comment, Featured, FeaturedMainImage

# Register your models here.
class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 10

class FeaturedMainImageInline(admin.TabularInline):
    model = FeaturedMainImage
    extra = 3

class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageInline]

class FeaturedAdmin(admin.ModelAdmin):
    inlines = [FeaturedMainImageInline]


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemImage)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Featured, FeaturedAdmin)
admin.site.register(FeaturedMainImage)
