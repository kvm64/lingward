# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# --- КОРТЕЖИ ДЛЯ ВЫБОРОВ ---
STATUS_CHOICES = (
    ('booked', 'Забронирован'),
    ('completed', 'Проведён'),
    ('cancelled', 'Отменён'),
    ('no_show', 'Неявка'),
)

LESSON_TYPE_CHOICES = (
    ('individual', 'Индивидуальный'),
    ('group', 'Групповой'),
)

class User(AbstractUser):
    ROLE_CHOICES = (
        ('tutor', 'Репетитор'),
        ('student', 'Ученик'),
        ('admin', 'Администратор'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    phone = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tutor_profile')
    bio = models.TextField(blank=True)
    languages = models.JSONField(default=list)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    rating = models.FloatField(default=0.0)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Репетитор: {self.user.username}"

    class Meta:
        verbose_name = "Репетитор"
        verbose_name_plural = "Репетиторы"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    level = models.CharField(max_length=2, blank=True)
    interests = models.JSONField(default=list)
    learning_goals = models.TextField(blank=True)

    def __str__(self):
        return f"Ученик: {self.user.username}"

    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"


class StudyGroup(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название группы")
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='study_groups')
    students = models.ManyToManyField(Student, related_name='study_groups', verbose_name="Ученики")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_active = models.BooleanField(default=True, verbose_name="Активна")

    class Meta:
        verbose_name = "Учебная группа"
        verbose_name_plural = "Учебные группы"
        ordering = ['name']

    def __str__(self):
        return self.name


class Lesson(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='lessons')
    lesson_type = models.CharField(max_length=10, choices=LESSON_TYPE_CHOICES, default='individual', verbose_name="Тип урока")
    study_group = models.ForeignKey(StudyGroup, on_delete=models.SET_NULL, null=True, blank=True, related_name='lessons', verbose_name="Учебная группа")
    students = models.ManyToManyField(Student, related_name='lessons', blank=True, verbose_name="Ученики")
    scheduled_at = models.DateTimeField(verbose_name="Дата и время")
    duration_minutes = models.IntegerField(default=60, verbose_name="Длительность (мин)")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='booked', verbose_name="Статус")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    videocall_room_id = models.CharField(max_length=255, blank=True, verbose_name="ID комнаты ВКС")
    whiteboard_session_id = models.CharField(max_length=255, blank=True, verbose_name="ID сессии доски")

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return f"Урок {self.tutor.user.username} → {self.study_group.name if self.study_group else 'индивидуальный'}"


class Review(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, related_name='review', verbose_name="Урок")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="Оценка")
    text = models.TextField(verbose_name="Текст отзыва")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_deleted = models.BooleanField(default=False, verbose_name="Удалён")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"Отзыв на урок #{self.lesson.id}"