from django.contrib import admin
from .models import Article, User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


class ArticleAdmin(admin.ModelAdmin):
    list_display =('id', 'title', 'text', 'author', 'for_subscribers', 'created_at', 'updated_at')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('for_subscribers',)

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_subscriber",
                    "is_author",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    list_display =('id', 'username', 'email', 'is_staff', 'is_subscriber', 'is_author', 'is_superuser', 'date_joined', 'updated_at')
    list_filter = ('is_staff', 'is_subscriber', 'is_author', 'is_superuser')
    list_display_links = ('id', 'username')

admin.site.register(Article, ArticleAdmin)
admin.site.register(User, CustomUserAdmin)

