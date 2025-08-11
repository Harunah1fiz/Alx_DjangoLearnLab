from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from  .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    """
    Extends the default Django UserAdmin so it works with our CustomUser model.
    Displays extra fields in admin forms and lists.
    """
        # Fields to display in the list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff','profile_photo','date_of_birth')
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('profile_photo', 'date_of_birth')}),
    )

    # Field groupings for the add user form
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('profile_photo', 'date_of_birth')}),
    )
    #fields that can be searched

    search_fields = ('username', 'email')

    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)