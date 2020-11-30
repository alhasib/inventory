from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Item)
admin.site.register(ProposeItem)
admin.site.register(AssignItem)
