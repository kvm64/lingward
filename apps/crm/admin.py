from django.contrib import admin
from .models import Tutor, Student, StudyGroup, Lesson, Review

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('user', 'price_per_hour', 'rating', 'is_verified')
    list_filter = ('is_verified', 'languages')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')
    ordering = ('-rating',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'level')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')

@admin.register(StudyGroup)
class StudyGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'tutor', 'is_active', 'created_at')
    list_filter = ('tutor', 'is_active')
    search_fields = ('name', 'tutor__user__username')
    filter_horizontal = ('students',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('tutor', 'study_group', 'scheduled_at', 'status', 'price')
    list_filter = ('status', 'scheduled_at')
    search_fields = ('tutor__user__username', 'study_group__name')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('lesson__tutor__user__username', 'lesson__study_group__name')