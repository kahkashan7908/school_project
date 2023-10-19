from django.contrib import admin
from .models import Teacher,Student,Certificate

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','course','taughtby']

class CertificateAdmin(admin.ModelAdmin):
    list_display = ['id', 'teacher','student','issue_date','jwt_token']

admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Certificate,CertificateAdmin)
