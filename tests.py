from django.test import TestCase
from django.urls import reverse
from .models import Student

class StudentManagementTests(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            admission_number="STU-001",
            full_name="Asha Kumar",
            email="asha@example.com",
            course="Computer Science",
            year=2,
        )

    def test_dashboard_loads(self):
        response = self.client.get(reverse("student_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Asha Kumar")

    def test_search_finds_student(self):
        response = self.client.get(reverse("student_list"), {"q": "STU-001"})
        self.assertContains(response, "Asha Kumar")

    def test_create_student(self):
        response = self.client.post(reverse("student_create"), {
            "admission_number": "STU-002",
            "full_name": "Ravi Shah",
            "email": "ravi@example.com",
            "course": "Business",
            "year": "1",
            "phone": "",
            "date_of_birth": "",
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Student.objects.filter(admission_number="STU-002").exists())

    def test_update_student(self):
        response = self.client.post(reverse("student_update", args=[self.student.pk]), {
            "admission_number": "STU-001",
            "full_name": "Asha K.",
            "email": "asha@example.com",
            "course": "Computer Science",
            "year": "3",
            "phone": "",
            "date_of_birth": "",
        })
        self.assertEqual(response.status_code, 302)
        self.student.refresh_from_db()
        self.assertEqual(self.student.full_name, "Asha K.")

    def test_delete_student(self):
        response = self.client.post(reverse("student_delete", args=[self.student.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Student.objects.filter(pk=self.student.pk).exists())
