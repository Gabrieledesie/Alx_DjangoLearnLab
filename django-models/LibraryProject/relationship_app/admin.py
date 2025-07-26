from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, Author, Book, Library, Librarian, Member, UserProfile, UserActionLog

# Custom User Admin
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'date_of_birth', 'profile_photo', 'password1', 'password2'),
        }),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_of_birth')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)


# Existing admin for Book with customization
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('author',)

admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(Member)
admin.site.register(UserProfile)
admin.site.register(UserActionLog)
