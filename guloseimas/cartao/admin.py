from django.contrib import admin
from .models import Cartao
from django.contrib.auth.models import User, Group

# Unregister
admin.site.unregister(User)
admin.site.unregister(Group)

# Register your models here.
admin.site.register(Cartao)
