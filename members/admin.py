from django.contrib import admin
from .models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin): #se crea una función 
    list_display = ("firstname", "lastname", "joined_date",) #detallamos que se va mostrar en usando list

admin.site.register(Member, MemberAdmin) #se registra al modelo
