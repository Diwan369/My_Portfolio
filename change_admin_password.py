#!/usr/bin/env python
"""
Script to change admin password
Run via: python manage.py shell < change_admin_password.py
"""

from django.contrib.auth.models import User

try:
    admin_user = User.objects.get(username='admin')
    admin_user.set_password('Missionself@9192')
    admin_user.save()
    print("✅ Admin password changed successfully!")
    print(f"Username: admin")
    print(f"New password: Missionself@9192")
except User.DoesNotExist:
    print("❌ Admin user not found. Creating new admin user...")
    User.objects.create_superuser('admin', 'admin@example.com', 'Missionself@9192')
    print("✅ Admin user created successfully!")
    print(f"Username: admin")
    print(f"Password: Missionself@9192")
except Exception as e:
    print(f"❌ Error: {e}")
