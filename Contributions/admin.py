from django.contrib import admin
from Contributions.models import CollegeContrib,DepartmentContrib,IndexedJournal

# Register your models here.

admin.site.register(CollegeContrib)
admin.site.register(DepartmentContrib)
admin.site.register(IndexedJournal)

admin.site.site_header = 'SKCT'