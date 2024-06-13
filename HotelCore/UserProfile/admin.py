from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.models import User

from UserProfile.models import UserProfiles


class UserInHotel(admin.StackedInline):
    model = UserProfiles
    can_delete = False
    verbose_name_plural = "userprofile"


class UserAdmin(UserAdmin):
    inlines = [UserInHotel]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
