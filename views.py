from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import StudentForm
from .models import Student

def student_list(request):
    query = request.GET.get("q", "").strip()
    students = Student.objects.all()
    if query:
        students = students.filter(
            Q(full_name__icontains=query) |
            Q(admission_number__icontains=query) |
            Q(email__icontains=query) |
            Q(course__icontains=query)
        )
    return render(request, "students/student_list.html", {
        "students": students,
        "query": query,
        "total_students": Student.objects.count(),
    })

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "students/student_detail.html", {"student": student})

def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, f"{student.full_name} was added successfully.")
            return redirect("student_detail", pk=student.pk)
    else:
        form = StudentForm()
    return render(request, "students/student_form.html", {"form": form, "page_title": "Add student"})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student details were updated.")
            return redirect("student_detail", pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, "students/student_form.html", {
        "form": form, "page_title": "Edit student", "student": student
    })

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        name = student.full_name
        student.delete()
        messages.success(request, f"{name} was deleted.")
        return redirect("student_list")
    return render(request, "students/student_confirm_delete.html", {"student": student})
