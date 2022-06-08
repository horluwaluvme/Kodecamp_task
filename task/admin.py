from django.contrib import admin
from .models import Product,People,Address,Bio,Doctor 

# Register your models here.
admin.site.register(Product)
admin.site.register(People)
admin.site.register(Address)
admin.site.register(Bio)
admin.site.register(Doctor)