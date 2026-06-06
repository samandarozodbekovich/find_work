#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

python manage.py shell << 'EOF'
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
EOF