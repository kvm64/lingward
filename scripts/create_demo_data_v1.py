import os
import sys
import django

# Добавляем путь к корню проекта
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
from apps.crm.models import Tutor, Student, StudyGroup, Lesson, Review
from decimal import Decimal
from datetime import datetime, timedelta

User = get_user_model()

def create_demo_data():
    print("🚀 Начинаем создание демонстрационных данных...")

    # --- 1. МЕНЕДЖЕР ---
    manager, _ = User.objects.get_or_create(
        username='manager',
        defaults={
            'email': 'manager@lingward.online',
            'first_name': 'Менеджер',
            'role': 'admin',
            'is_active': True,
            'is_staff': True,
            'is_superuser': True,
        }
    )
    manager.set_password('manager123')
    manager.save()
    print("✅ Менеджер создан.")

    # --- 2. РЕПЕТИТОРЫ ---
    tutor1_user, _ = User.objects.get_or_create(
        username='anna.petrova',
        defaults={
            'email': 'anna@lingward.online',
            'first_name': 'Анна',
            'last_name': 'Петрова',
            'role': 'tutor',
            'is_active': True,
        }
    )
    tutor1_user.set_password('tutor123')
    tutor1_user.save()

    tutor1, _ = Tutor.objects.get_or_create(
        user=tutor1_user,
        defaults={
            'bio': 'Репетитор английского языка. Опыт 5 лет.',
            'languages': ['Английский'],
            'price_per_hour': Decimal('2500.00'),
            'rating': 4.8,
            'is_verified': True,
        }
    )
    print("✅ Анна Петрова создана.")

    tutor2_user, _ = User.objects.get_or_create(
        username='ivan.smirnov',
        defaults={
            'email': 'ivan@lingward.online',
            'first_name': 'Иван',
            'last_name': 'Смирнов',
            'role': 'tutor',
            'is_active': True,
        }
    )
    tutor2_user.set_password('tutor123')
    tutor2_user.save()

    tutor2, _ = Tutor.objects.get_or_create(
        user=tutor2_user,
        defaults={
            'bio': 'Репетитор французского языка. Носитель.',
            'languages': ['Французский'],
            'price_per_hour': Decimal('3000.00'),
            'rating': 4.5,
            'is_verified': True,
        }
    )
    print("✅ Иван Смирнов создан.")

    # --- 3. УЧЕНИКИ (ГРУППА АННЫ) ---
    group_students = []
    group_names = [
        ('elena.egorova', 'Елена', 'Егорова'),
        ('mikhail.sidorov', 'Михаил', 'Сидоров'),
        ('olga.borisova', 'Ольга', 'Борисова'),
        ('alexey.vasiliev', 'Алексей', 'Васильев'),
        ('maria.grigorieva', 'Мария', 'Григорьева'),
    ]

    for username, first, last in group_names:
        user, _ = User.objects.get_or_create(
            username=username,
            defaults={
                'email': f'{username}@lingward.online',
                'first_name': first,
                'last_name': last,
                'role': 'student',
                'is_active': True,
            }
        )
        user.set_password('student123')
        user.save()

        student, _ = Student.objects.get_or_create(
            user=user,
            defaults={
                'level': 'B1',
                'interests': ['разговорный', 'грамматика'],
                'learning_goals': 'Свободное владение английским',
            }
        )
        group_students.append(student)
        print(f"✅ {first} {last} создан(а).")

    # --- 4. УЧЕБНАЯ ГРУППА ---
    study_group, _ = StudyGroup.objects.get_or_create(
        name='Group-EN-01',
        defaults={
            'tutor': tutor1,
            'is_active': True,
        }
    )
    study_group.students.set(group_students)
    print("✅ Учебная группа Group-EN-01 создана.")

    # --- 5. ИНДИВИДУАЛЬНЫЕ УЧЕНИКИ (ИВАН) ---
    individual_students = []
    individual_names = [
        ('dmitry.grishin', 'Дмитрий', 'Гришин'),
        ('anna.davydova', 'Анна', 'Давыдова'),
        ('sergey.dmitriev', 'Сергей', 'Дмитриев'),
        ('ekaterina.fedorova', 'Екатерина', 'Фёдорова'),
        ('andrey.kuznetsov', 'Андрей', 'Кузнецов'),
    ]

    for username, first, last in individual_names:
        user, _ = User.objects.get_or_create(
            username=username,
            defaults={
                'email': f'{username}@lingward.online',
                'first_name': first,
                'last_name': last,
                'role': 'student',
                'is_active': True,
            }
        )
        user.set_password('student123')
        user.save()

        student, _ = Student.objects.get_or_create(
            user=user,
            defaults={
                'level': 'A2',
                'interests': ['путешествия', 'кулинария'],
                'learning_goals': 'Общение в поездках',
            }
        )
        individual_students.append(student)
        print(f"✅ {first} {last} создан(а).")

    # --- 6. УРОКИ ---
    now = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)

    lesson1, _ = Lesson.objects.get_or_create(
        tutor=tutor1,
        study_group=study_group,
        scheduled_at=now + timedelta(days=0),
        defaults={
            'lesson_type': 'group',
            'duration_minutes': 90,
            'status': 'booked',
            'price': Decimal('2500.00'),
        }
    )
    print("✅ Групповой урок создан.")

    lesson2, _ = Lesson.objects.get_or_create(
        tutor=tutor1,
        study_group=study_group,
        scheduled_at=now + timedelta(days=1),
        defaults={
            'lesson_type': 'group',
            'duration_minutes': 90,
            'status': 'booked',
            'price': Decimal('2500.00'),
        }
    )
    print("✅ Второй групповой урок создан.")

    lesson3, _ = Lesson.objects.get_or_create(
        tutor=tutor2,
        scheduled_at=now + timedelta(hours=2),
        defaults={
            'lesson_type': 'individual',
            'duration_minutes': 60,
            'status': 'completed',
            'price': Decimal('3000.00'),
        }
    )
    lesson3.students.set([individual_students[0]])
    print("✅ Индивидуальный урок (проведён) создан.")

    lesson4, _ = Lesson.objects.get_or_create(
        tutor=tutor2,
        scheduled_at=now + timedelta(days=1, hours=4),
        defaults={
            'lesson_type': 'individual',
            'duration_minutes': 60,
            'status': 'booked',
            'price': Decimal('3000.00'),
        }
    )
    lesson4.students.set([individual_students[1]])
    print("✅ Индивидуальный урок (забронирован) создан.")

    # --- 7. ОТЗЫВЫ ---
    review1, _ = Review.objects.get_or_create(
        lesson=lesson3,
        defaults={
            'rating': 5,
            'text': 'Отличный урок! Иван очень понятно объясняет.',
            'is_deleted': False,
        }
    )
    print("✅ Отзыв создан.")

    print("🎉 Демонстрационные данные успешно созданы!")

if __name__ == '__main__':
    create_demo_data()