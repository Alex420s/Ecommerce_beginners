from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile) # register a module to admin 
class UserProfileAdmin(admin.ModelAdmin):
    # List the fields you want to display
    list_display = ('id', 'user', 'created')