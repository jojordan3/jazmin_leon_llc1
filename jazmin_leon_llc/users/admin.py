from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.contrib import admin
#from myapp.models import Author
#from guardian.admin import GuardedModelAdmin

# Old way:
#class AuthorAdmin(admin.ModelAdmin):
#    pass

# With object permissions support
#class AuthorAdmin(GuardedModelAdmin):
#    pass

#admin.site.register(Author, AuthorAdmin)

from jazmin_leon_llc.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]
