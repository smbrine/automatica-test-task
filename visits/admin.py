from django.contrib import admin

# visits/admin.py
from django.contrib import admin
from .models import Worker, RetailPoint, Visit

class WorkerAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'phone']

class RetailPointAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'worker']

class VisitAdmin(admin.ModelAdmin):
    search_fields = ['worker__name', 'retail_point__name']
    list_display = ['retail_point', 'worker', 'datetime']

admin.site.register(Worker, WorkerAdmin)
admin.site.register(RetailPoint, RetailPointAdmin)
admin.site.register(Visit, VisitAdmin)
