from django.contrib import admin

from .models import MenuCategory, MenuItem, OpeningHour, Store

admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(OpeningHour)
admin.site.register(Store)
