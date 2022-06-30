from django.contrib import admin
from asset.models import AssetCash

admin.site.register(AssetCash)


class AssetCashAdmin(admin.ModelAdmin):
    fields = ('title', 'remark')
    list_editable = ['title', 'remark']
