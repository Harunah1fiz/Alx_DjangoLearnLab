from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
    
admin.site.register(Book)


class CustomUserAdmin(UserAdmin):
    """
    Extends the default Django UserAdmin so it works with our CustomUser model.
    Displays extra fields in admin forms and lists.
    """

        #Field to display in the list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'profile_photo', 'date_of_birth')

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