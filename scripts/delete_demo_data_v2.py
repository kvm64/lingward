import os
import sys
import django

# Добавляем путь к корню проекта
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
from apps.crm.models import Tutor, Student, StudyGroup, Lesson, Review

User = get_user_model()

def delete_demo_data():
    print("🧹 Начинаем удаление демонстрационных данных (v2)...")

    Review.objects.filter(
        lesson__tutor__user__username__in=['anna.petrova', 'ivan.smirnov']
    ).delete()
    print("✅ Отзывы удалены.")

    Lesson.objects.filter(
        tutor__user__username__in=['anna.petrova', 'ivan.smirnov']
    ).delete()
    print("✅ Уроки удалены.")

    StudyGroup.objects.filter(
        tutor__user__username__in=['anna.petrova', 'ivan.smirnov']
    ).delete()
    print("✅ Учебные группы удалены.")

    Student.objects.filter(
        user__username__in=[
            'elena.egorova', 'mikhail.sidorov', 'olga.borisova',
            'alexey.vasiliev', 'maria.grigorieva',
            'dmitry.grishin', 'anna.davydova', 'sergey.dmitriev',
            'ekaterina.fedorova', 'andrey.kuznetsov'
        ]
    ).delete()
    print("✅ Студенты удалены.")

    Tutor.objects.filter(
        user__username__in=['anna.petrova', 'ivan.smirnov']
    ).delete()
    print("✅ Репетиторы удалены.")

    User.objects.filter(
        username__in=[
            'anna.petrova', 'ivan.smirnov',
            'elena.egorova', 'mikhail.sidorov', 'olga.borisova',
            'alexey.vasiliev', 'maria.grigorieva',
            'dmitry.grishin', 'anna.davydova', 'sergey.dmitriev',
            'ekaterina.fedorova', 'andrey.kuznetsov'
        ]
    ).delete()
    print("✅ Пользователи удалены.")

    print("🎉 Демонстрационные данные (v2) успешно удалены!")

if __name__ == '__main__':
    delete_demo_data()