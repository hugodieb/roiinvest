# admin.py
from django.contrib import admin
from .models import User, Profile 

# Registra o modelo User no admin
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'username', 'subscription_type']  # Campos a serem exibidos na lista
    search_fields = ['email', 'username']  # Campos para buscar

# Registra o modelo Profile no admin
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'birth_date', 'cpf', 'phone', 'avatar']
    search_fields = ['cpf', 'user__username']  # Campos para buscar

