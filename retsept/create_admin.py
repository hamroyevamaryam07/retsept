import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "retsept.settings"
)

django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

if not username or not email or not password:
    raise RuntimeError(
        "Render Environment bo'limida "
        "DJANGO_SUPERUSER_USERNAME, "
        "DJANGO_SUPERUSER_EMAIL va "
        "DJANGO_SUPERUSER_PASSWORD ni kiriting."
    )

user, created = User.objects.get_or_create(
    username=username,
    defaults={"email": email},
)

user.email = email
user.is_staff = True
user.is_superuser = True
user.is_active = True
user.set_password(password)
user.save()

print(f"Admin hisobi tayyor: {username}")