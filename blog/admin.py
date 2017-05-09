from django.contrib import admin
from . models import CompanyInfo, Videos, Pictures, Customer
# Register your models here.

admin.site.register(CompanyInfo)
admin.site.register(Videos)
admin.site.register(Pictures)
admin.site.register(Customer)
