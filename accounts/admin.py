from django.contrib import admin
from . models import UserManager
from . forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from . models import User



class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    # a form that using to add object(User)
    add_form = UserCreationForm


    list_display = ('phone_number', 'username', 'email')
    list_filter = ('is_admin', 'is_active')


    fieldsets = (
        (None, {
            'fields': ('phone_number', 'username', 'email', 'password')
            }),
        ('Permissions', {
            'fields': ('is_active', 'is_admin', 'groups', 'is_superuser', 'last_login')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('phone_number', 'pass1', 'pass2')
        }),
    )

    ordering = ('is_active', 'is_admin')
    search_fields = ('email', 'username', 'phone_number')
    filter_horizontal = ('groups',)
    readonly_fields = ('last_login',)



admin.site.register(User, UserAdmin)