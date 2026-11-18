from django.db import models

class Student(models.Model):
    YEAR_CHOICES = [(1, "Year 1"), (2, "Year 2"), (3, "Year 3"), (4, "Year 4")]
    admission_number = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField(choices=YEAR_CHOICES, default=1)
    phone = models.CharField(max_length=25, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["full_name"]

    def __str__(self):
        return f"{self.full_name} ({self.admission_number})"
