from django.contrib import admin

from .models import Reply, Room, User

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Reply)