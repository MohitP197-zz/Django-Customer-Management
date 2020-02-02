from django.contrib import admin

# Register your models here.

# Imports all the models
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
