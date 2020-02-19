from django.contrib import admin

from admin_ordering.admin import OrderableAdmin

from workbench.deals import models


class ValueInline(admin.TabularInline):
    model = models.Value
    extra = 0


@admin.register(models.Deal)
class DealAdmin(admin.ModelAdmin):
    inlines = [ValueInline]
    list_display = ["title", "owned_by", "value", "status", "created_at"]
    list_filter = ["status"]
    raw_id_fields = ["customer", "contact", "owned_by"]
    search_fields = ["title", "description"]


@admin.register(models.Stage)
class StageAdmin(OrderableAdmin, admin.ModelAdmin):
    list_display = ["title", "position"]
    list_editable = ["position"]
    ordering_field = "position"


@admin.register(models.ValueType)
class ValueTypeAdmin(OrderableAdmin, admin.ModelAdmin):
    list_display = ["title", "position"]
    list_editable = ["position"]
    ordering_field = "position"


@admin.register(models.Source)
class SourceAdmin(OrderableAdmin, admin.ModelAdmin):
    list_display = ["title", "position"]
    list_editable = ["position"]
    ordering_field = "position"


@admin.register(models.Sector)
class SectorAdmin(OrderableAdmin, admin.ModelAdmin):
    list_display = ["title", "position"]
    list_editable = ["position"]
    ordering_field = "position"


@admin.register(models.ClosingType)
class ClosingType(OrderableAdmin, admin.ModelAdmin):
    list_display = ["title", "is_won", "position"]
    list_editable = ["position"]
    ordering_field = "position"
