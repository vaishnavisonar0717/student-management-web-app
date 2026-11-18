from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("admission_number", "full_name", "email", "course", "year")
    search_fields = ("admission_number", "full_name", "email", "course")
    list_filter = ("year", "course")
