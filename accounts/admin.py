from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Product_Request)
admin.site.register(Vendor)
admin.site.register(Client_Order)
admin.site.register(Vendor_Order)
admin.site.register(Tag)
