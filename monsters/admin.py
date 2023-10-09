from django.contrib import admin
from .models import Monster

# Register your models here.


class MonsterAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "level"]
    list_filter = [
        "level",
    ]


admin.site.register(Monster, MonsterAdmin)
