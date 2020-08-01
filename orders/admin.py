from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Regularpizza)
admin.site.register(Topping)
admin.site.register(Sicilianpizza)
admin.site.register(Extra)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Subs)
admin.site.register(Dinnerplatter)
admin.site.register(Menuitem)
admin.site.register(Order)