from django.contrib import admin

# Register your models here.
from skct.models import Proof,Staff,It,Cse,Mech,Eee,Ece,Civil,Ice,Sh,Mba,Hod,ProfDisplay

admin.site.register(Proof)
admin.site.register(Staff)
admin.site.register(It)
admin.site.register(Cse)
admin.site.register(Mech)
admin.site.register(Eee)
admin.site.register(Ece)
admin.site.register(Civil)
admin.site.register(Ice)
admin.site.register(Sh)
admin.site.register(Mba)
admin.site.register(Hod)
admin.site.register(ProfDisplay)

admin.site.site_header='SKCT'   