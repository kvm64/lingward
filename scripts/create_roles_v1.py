import os
import sys
import django

# Добавляем путь к корню проекта
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import Group

def create_roles():
    print("🔧 Создание системных ролей...")
    roles = ['Manager', 'Tutor', 'Student', 'Administrator']
    for role in roles:
        group, created = Group.objects.get_or_create(name=role)
        if created:
            print(f"✅ Роль '{role}' создана.")
        else:
            print(f"ℹ️ Роль '{role}' уже существует.")
    print("🎉 Системные роли созданы!")

if __name__ == '__main__':
    create_roles()