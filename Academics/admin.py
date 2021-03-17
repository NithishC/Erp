from django.contrib import admin
from .models import Academics,Feedback,Innovation,UG,PG,ExtraCurricular,AllClear,ThreeClear,Article,Competitive,Startups,Awards,Prizes,Internship,OnlineCertification
# Register your models here.

admin.site.register(Academics)
admin.site.register(Feedback)
admin.site.register(Innovation)
admin.site.register(UG)
admin.site.register(PG)
admin.site.register(ExtraCurricular)
admin.site.register(AllClear)
admin.site.register(ThreeClear)
admin.site.register(Article)
admin.site.register(Competitive)
admin.site.register(Startups)
admin.site.register(Awards)
admin.site.register(Prizes)
admin.site.register(Internship)
admin.site.register(OnlineCertification)

admin.site.site_header='SKCT'   