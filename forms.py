from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["admission_number", "full_name", "email", "course", "year", "phone", "date_of_birth"]
        widgets = {
            "admission_number": forms.TextInput(attrs={"placeholder": "e.g. STU-2026-001"}),
            "full_name": forms.TextInput(attrs={"placeholder": "Enter student's full name"}),
            "email": forms.EmailInput(attrs={"placeholder": "student@example.com"}),
            "course": forms.TextInput(attrs={"placeholder": "e.g. Computer Science"}),
            "phone": forms.TextInput(attrs={"placeholder": "Optional phone number"}),
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
        }
