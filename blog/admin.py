from django.contrib import admin

from . models import CompanyInfo, Video, Picture, Customer, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Video)
admin.site.register(Customer)
admin.site.register(Picture)


@admin.register(CompanyInfo)
class CompanyInfoView(admin.ModelAdmin):

    list_display = ('co_name', 'logo', 'short_description')
    fieldsets = (
        (None, {
            'fields': ('co_name', 'logo', 'short_description')
    }),
        ('Contact Information', {
            'fields': ('address1','address2', 'position', 'phone_number', 'instagram')
        }
        )
    )

