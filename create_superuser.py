import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'find_work.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

username = 'admin1'
password = 'admin1234'

if User.objects.filter(username=username).exists():
    u = User.objects.get(username=username)
    u.is_staff = True
    u.is_superuser = True
    u.set_password(password)
    u.save()
    print("Superuser yangilandi")
else:
    User.objects.create_superuser(username, 'admin1@mail.com', password)
    print("Superuser yaratildi")