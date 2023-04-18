from django.contrib import admin

from Thread.models import Thread, Message

# Register your models here.
admin.site.register(Thread)
admin.site.register(Message)