from django.contrib import admin

from .models import *

admin.site.register(SystemAdmin)
admin.site.register(AssociationsManager)
admin.site.register(Association)
admin.site.register(Members)
admin.site.register(Event)
admin.site.register(Attend)
admin.site.register(Staff)
admin.site.register(myUser)


