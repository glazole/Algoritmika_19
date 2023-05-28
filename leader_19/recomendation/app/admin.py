from django.contrib import admin
from .models import UserId
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import UserIdCreationForm, UserIdChangeForm


class UserIdAdmin(UserAdmin):
    add_form = UserIdCreationForm
    form = UserIdChangeForm
    model = UserId
  #  list_display = ['username', 'added_at', 'sex', 'address', 'birth_date']
  #  fieldsets = UserAdmin.fieldsets + (
  #          (None, {'fields': ('added_at', 'sex', 'address', 'birth_date')}),
  #  )


   # list_display = ['username', 'added_at', 'sex', 'address', 'birth_date']
   # fieldsets = UserAdmin.fieldsets + (
   #         (None, {'fields': ('added_at', 'sex', 'address', 'birth_date')}),
   # ) #this will allow to change these fields in admin module


admin.site.register(UserId, UserIdAdmin)

