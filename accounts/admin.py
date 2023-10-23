from django.contrib import admin

from django.contrib.auth.models import Group ,User

from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile

#extend user models 
class UserAdmin(admin.ModelAdmin):
    models  = User
    fields = ['username']
    inlines  = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User,UserAdmin)
