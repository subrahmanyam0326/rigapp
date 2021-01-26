from django.contrib import admin
from riggpp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name','age','location']
admin.site.register(Employee,EmployeeAdmin)
