from django.contrib import admin
from .models import Bala

# Register your models here.
@admin.register(Bala)
class PostAdmin(admin.ModelAdmin):
  list_display = ("nome", "quantidade", "preco")

