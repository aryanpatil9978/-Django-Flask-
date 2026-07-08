from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'full_name', 'created_at', 'updated_at')
    search_fields = ('username', 'email', 'full_name')
    list_filter = ('created_at', 'updated_at')
