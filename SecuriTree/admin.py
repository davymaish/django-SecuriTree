from django.contrib import admin
from django.contrib.auth.models import Group


# Register your models here.

from .models import Door, Area, User, AccessRule, UserAccessRule, DoorAccessRule

class UserAccessInline(admin.TabularInline):
    model = UserAccessRule
    extra = 0

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['username', 'first_name', 'surname', 'password']}),
        ('Date information', {'fields': ['date_joined']}),
    ]
    inlines = [UserAccessInline]
    list_display = ('username', 'first_name', 'surname')
    list_filter = ['date_joined']
    search_fields = ['username', 'first_name', 'surname']

class DoorAccessInline(admin.TabularInline):
    model = DoorAccessRule
    extra = 2

class DoorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['id', 'name', 'parent_area', 'status']}),
    ]
    inlines = [DoorAccessInline]
    list_display = ('id', 'name', 'parent_area', 'status')
    list_filter = ['parent_area', 'status']
    search_fields = ['id', 'name', 'parent_area', 'status']

class AreaDoorInline(admin.TabularInline):
    model = Door
    extra = 0

class AreaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['id', 'name', 'parent_area']}),
    ]
    inlines = [AreaDoorInline]
    list_display = ('id', 'name', 'parent_area')
    list_filter = ['parent_area']
    search_fields = ['id', 'name', 'parent_area']

class AccessAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['id', 'name']}),
    ]
    list_display = ('id', 'name')
    list_filter = ['doors']
    search_fields = ['id', 'name']

admin.site.register(User, UserAdmin)
admin.site.register(Door, DoorAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(AccessRule, AccessAdmin)
admin.site.unregister(Group)