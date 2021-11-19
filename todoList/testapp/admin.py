from django.contrib import admin
from testapp.models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['name','desc','time']

admin.site.register(Task,TaskAdmin)    
