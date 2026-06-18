from django.db import connection
from .models import (
    ChessPuzzle,
    Achievement,
    LessonProgress,
    OpeningProgress,
)


def check_database():
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return True
    except Exception:
        return False


def check_puzzles():
    try:
        ChessPuzzle.objects.exists()
        return True
    except Exception:
        return False


def check_achievements():
    try:
        Achievement.objects.exists()
        return True
    except Exception:
        return False


def check_lessons():
    try:
        LessonProgress.objects.exists()
        return True
    except Exception:
        return False


def check_openings():
    try:
        OpeningProgress.objects.exists()
        return True
    except Exception:
        return False
