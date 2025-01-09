from django.contrib import admin

# Register your models here.
from Packages_Section.models import Packages_Section

class Packages_Section_Admin(admin.ModelAdmin):
    list_display = ['first_section_title','first_section_info','second_section_title', 'second_section_info' ]

admin.site.register(Packages_Section,Packages_Section_Admin)