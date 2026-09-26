from django.contrib import admin
from products.models import Product,Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug':('title',)}
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title"]
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)