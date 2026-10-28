
from django.db import models


class Recipe(models.Model):
    nom = models.CharField(max_length=200, null=True)
    tavsif = models.TextField(null=True)

    tur = models.CharField(
        max_length=100,
        default="Boshqa",
        null=True
    )

    vaqt = models.CharField(max_length=50, null=True)
    rasm = models.URLField(blank=True, null=True)

    masalliqlar = models.TextField(
        default="",
        null=True,
        blank=True,
        help_text="Har bir masalliqni yangi qatordan yozing"
    )

    tayyorlash_usuli = models.TextField(
        default="",
        null=True,
        blank=True,
        help_text="Taomni tayyorlash bosqichlarini yozing"
    )

    yaratilgan_vaqt = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ["-yaratilgan_vaqt"]

    def __str__(self):
        return self.nom or "Nomsiz retsept"
