from django.contrib import admin
from . models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'stripe_id', 'date_of_birth', 'photo']