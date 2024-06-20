from django.contrib import admin

# Register your models here.
from .models import Product, Contact, Orders, OrderUpdate

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)











#username - lokesh
#password - 1234
# emailid - lokesh@gmail.com


# Pending Topic - tracker , payment gateway
# py manage.py changepassword or create superuser