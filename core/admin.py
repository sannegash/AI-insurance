from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User

# Create a custom UserAdmin to ensure password is hashed
class CustomUserAdmin(UserAdmin):
    model = User
    # Customizes the form to ensure password is handled correctly in the admin panel
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'birth_date', 'gender', 'postal_code', 'city', 'state', 'status')}),
        (_('Permissions'), {'fields': ('role',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'birth_date', 'gender', 'postal_code', 'city', 'state', 'role'),
        }),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'status', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

# Register the custom user admin
admin.site.register(User, CustomUserAdmin)
