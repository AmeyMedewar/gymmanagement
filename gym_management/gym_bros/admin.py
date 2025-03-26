from django.contrib import admin
from .models import Member, Trainer, Schedule, Payment, Attendance

admin.site.register(Member)
admin.site.register(Trainer)
admin.site.register(Schedule)
admin.site.register(Payment)
admin.site.register(Attendance)
