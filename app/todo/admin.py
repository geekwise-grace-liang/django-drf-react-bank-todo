from django.contrib import admin
from .models import Branch, Customer

class BranchAdmin(admin.ModelAdmin):
    list_display = ('bank_name', 'location')
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'phone_number', 'email', 'address')

# Register your models here.

admin.site.register(Branch, BranchAdmin)
admin.site.register(Customer, CustomerAdmin)