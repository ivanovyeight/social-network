from django.contrib import admin

from account.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'stripe_id', 'paid_until', 'date_of_birth', 'photo']
