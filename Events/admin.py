from django.contrib import admin
from Events.models import Grant,InternationalConf,NationalConf,Workshop,FDP,InterCollege,InternationalConf2,InterCollege2,Workshop2,FDP2,NationalConf2

# Register your models here.

admin.site.register(Grant)
admin.site.register(InternationalConf)
admin.site.register(InterCollege)
admin.site.register(Workshop)
admin.site.register(FDP)
admin.site.register(NationalConf)
admin.site.register(InternationalConf2)
admin.site.register(InterCollege2)
admin.site.register(Workshop2)
admin.site.register(FDP2)
admin.site.register(NationalConf2)

admin.site.site_header='SKCT'   