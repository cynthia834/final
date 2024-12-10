from django.contrib import admin

from Bike.models import Bicycle,Member,CheckIn,Owner,ImageModel

# Register your models here.
admin.site.register(Bicycle)
admin.site.register(Member)
admin.site.register(Owner)
admin.site.register(CheckIn)
admin.site.register(ImageModel)

