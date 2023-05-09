from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'created_at')
    list_display_links = ('id', 'username')
    list_editable = ()
    search_fields = ('id', 'username')
    list_filter = ()


admin.site.register(User, UserAdmin)
