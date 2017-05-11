from django.contrib import admin

from . models import CompanyInfo, Video, Picture, Customer, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Customer)
admin.site.register(Picture)
admin.site.register(Video)



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

    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = CompanyInfo.objects.all().count()
        if count == 0:
            return True
        return False

    def image_img(self):
        if self.image:
            return u'<img src="%s" />' % self.image.url
        else:
            return '(No image found)'

    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

