from django.contrib import admin
from .models import Item, ItemImage

class ItemImageInline(admin.TabularInline):  # หรือ admin.StackedInline ตามที่คุณต้องการ
    model = ItemImage
    extra = 1  # จำนวนฟอร์มเพิ่มเติมที่แสดงในหน้าแสดงรายละเอียดของ Item

class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageInline]

# Register your models here.
admin.site.register(Item, ItemAdmin)