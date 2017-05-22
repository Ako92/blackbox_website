from django.contrib import admin
# from django.contrib.gis.db import models


from . models import CompanyInfo, Video, Picture, Customer, Profile, SocialAccount

# Register your models here.
admin.site.register(Profile)
admin.site.register(Customer)
admin.site.register(Picture)
admin.site.register(Video)


class SocialAccountsInline(admin.StackedInline):
    model = SocialAccount
    max_num = 10
    extra = 1


class CompanyInfoAdmin(admin.ModelAdmin):
    inlines = [
        SocialAccountsInline,
    ]

admin.site.register(CompanyInfo,CompanyInfoAdmin)


"""" @admin.register(CompanyInfo)
class CompanyInfoView(admin.ModelAdmin):

    list_display = ('co_name', 'short_description','logo')
    fieldsets = (
        (None, {
            'fields': ('co_name', 'logo', 'short_description', 'user'),

        }),
        ('Contact Information', {
            'fields': ('address1', 'address2', 'position', 'phone_number')
        }
         )
    )

    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = CompanyInfo.objects.all().count()
        if count == 0:
            return True
        return False
"""