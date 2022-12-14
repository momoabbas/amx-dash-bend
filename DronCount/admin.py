from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CountDetails)

admin.site.register(GMap)
admin.site.register(Drone)

admin.site.register(Log)


# from django.contrib import admin
# from django_google_maps import widgets as map_widgets
# from django_google_maps import fields as map_fields
#
# class GMapAdmin(admin.ModelAdmin):
#      formfield_overrides = {
#         map_fields.AddressField: {
#           'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
#     }
