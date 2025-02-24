from django.contrib import admin
from .models import Emp,Testimonial
# Register your models here.


class EmpAdmin(admin.ModelAdmin):
    list_display = ('name','emp_id','phone','working')
    list_editable = ('phone',)
    search_fields = ('name',)
    list_filter = ('emp_id',)


admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)