from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _  # Import this line
from .models import User 
from accounts.models import NewCustomer
# Inline admin to manage NewCustomer fields directly in the User admin
class NewCustomerInline(admin.StackedInline):
    model = NewCustomer
    fields = ('status',)  # Only show the status field in the inline admin
    can_delete = False
    verbose_name_plural = 'New Customer Info'

# Customizing UserAdmin to include NewCustomer inline
class CustomUserAdmin(admin.ModelAdmin):
    model = User

    # Method to fetch the status from the NewCustomer model
    def get_status(self, obj):
        try:
            return obj.newcustomer.status  # Access the status from the related NewCustomer model
        except NewCustomer.DoesNotExist:
            return 'No Status'

    get_status.short_description = 'Status'  # Label in the admin

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'birth_date', 'gender')}),
        (_('Permissions'), {'fields': ('role',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'birth_date', 'gender', 'role'),
        }),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'get_status', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

    # Include the NewCustomerInline in the UserAdmin
    inlines = [NewCustomerInline]

# Register the custom user admin
admin.site.register(User, CustomUserAdmin)
