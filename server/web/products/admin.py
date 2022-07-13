import logging
from django.contrib import admin

from web.products.models import Accessory, Vehicle

log = logging.getLogger(__name__)

# Register your models here.
admin.site.register(Vehicle)


@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    """
    """
    fields = ('unicode_name', )

    def save_model(self, request, obj, form, change):
        """
        """
        log.info('hello world')
        return 0
