
from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = [
        "nom",
        "tavsif",
        "tur",
        "vaqt",
        "rasm",
        "masalliqlar",
        "tayyorlash_usuli",
    ]

    def get_fieldsets(self, request, obj=None):
        return [
            ("Qo'shish recipe", {
                "fields": self.fields
            })
        ]
