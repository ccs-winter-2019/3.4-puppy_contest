from django.contrib import admin

from .models import Photo, Contest


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 3


class ContestAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(Photo)
admin.site.register(Contest, ContestAdmin)
