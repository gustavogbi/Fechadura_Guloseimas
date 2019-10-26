import csv
from django.contrib import admin
from .models import Cartao
from django.contrib.auth.models import User, Group
from django.http import HttpResponse

# Unregister
admin.site.unregister(User)
admin.site.unregister(Group)

# Register your models here.
#admin.site.register(Cartao)

@admin.register(Cartao)
class CartaoAdmin(admin.ModelAdmin):
  actions = ["atualizar_saldo"]
  def atualizar_saldo(self, request, queryset):
    meta = self.model._meta
    field_names = [field.name for field in meta.fields]
    obj = queryset[0]
    response = HttpResponse(content_type='text/txt')
    response['Content-Disposition'] = 'attachment; filename={}.txt'.format(getattr(obj, 'codigo'))
    writer = csv.writer(response)
    writer.writerow([getattr(obj, 'saldo')])
    #writer.writerow(field_names)
    #for obj in queryset:
      #row = writer.writerow([getattr(obj, field) for field in field_names])

    return response
  atualizar_saldo.short_description = "Atualizar Saldo"