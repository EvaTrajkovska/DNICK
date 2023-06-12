from django.contrib import admin
from .models import Car, Manufacturer, ManufWorkshop, Workshop, Fix
# Register your models here.


class ManufWorkshopAdmin(admin.TabularInline):
    model = ManufWorkshop
    extra = 0


class WorkshopAdmin(admin.ModelAdmin):
    inlines = [ManufWorkshopAdmin,]
    list_display = ("name", "year")


admin.site.register(Workshop, WorkshopAdmin)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("manuf_name",)

    def has_add_permission(self, request):
        return request.user.is_superuser


admin.site.register(Manufacturer, ManufacturerAdmin)


class CarAdmin(admin.ModelAdmin):
    list_display = ("type", "max_speed")


admin.site.register(Car, CarAdmin)


class FixAdmin(admin.ModelAdmin):
    exclude = ("user", )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Fix, FixAdmin)


