from django.contrib import admin

from .models.contribution import Contribution
from .models.project import Project


class BaseModelAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Project, BaseModelAdmin)
admin.site.register(Contribution, BaseModelAdmin)
