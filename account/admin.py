from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Organization, UserProfile,CountiesModel,CitiesModel,skills
from .resource import CountryResource,CitiesResource,SkillsResource
from import_export.admin import ImportExportModelAdmin

class OrganizationInline(admin.StackedInline):
    model = Organization
    can_delete = False
    verbose_name_plural = 'Organization'

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    inlines = (OrganizationInline,)
    list_display = ('email', 'username', 'is_organization', 'is_staff', 'is_active')
    list_filter = ('is_organization', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'phone_number', 'is_organization')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'phone_number', 'is_organization', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Organization)
admin.site.register(UserProfile)

@admin.register(CountiesModel)
class CountryAdmin(ImportExportModelAdmin):
    resource_class = CountryResource

@admin.register(CitiesModel)
class CountryAdmin(ImportExportModelAdmin):
    resource_class = CitiesResource

@admin.register(skills)
class CountryAdmin(ImportExportModelAdmin):
    resource_class = SkillsResource