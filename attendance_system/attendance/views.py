from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q  # Q importi to‘g‘ri
from .models import Student, Attendance
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import csv
from django.http import HttpResponse



@login_required
def download_csv(request):
    # Javob turini CSV qilib belgilaymiz
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="attendance_report.csv"'

    writer = csv.writer(response)
    # Header
    writer.writerow(['Username', 'Roll No', 'Department', 'Presents', 'Absents', 'Total Classes', 'Status'])

    # Data
    students = Student.objects.annotate(
        total_classes=Count('attendance'),
        presents=Count('attendance', filter=Q(attendance__status='Present')),
        absents=Count('attendance', filter=Q(attendance__status='Absent'))
    )

    for s in students:
        status = 'Warning' if s.absents > 3 else 'Good'
        writer.writerow([s.user.username, s.roll_number, s.department, s.presents, s.absents, s.total_classes, status])

    return response

# Dashboard
@login_required
def dashboard(request):
    students = Student.objects.all()
    return render(request, 'attendance/dashboard.html', {'students': students})

# Mark Attendance
@login_required
def mark_attendance(request):
    if request.method == "POST":
        for key, value in request.POST.items():
            if key.startswith('student_'):
                student_id = key.split('_')[1]
                status = value
                try:
                    student = Student.objects.get(id=student_id)
                    Attendance.objects.create(student=student, status=status)
                except Student.DoesNotExist:
                    continue  # Agar student topilmasa davom etadi
        return redirect('dashboard')

    students = Student.objects.all()
    return render(request, 'attendance/mark_attendance.html', {'students': students})

# Attendance Report
@login_required
def report(request):
    report_data = Student.objects.annotate(
        total_classes=Count('attendance'),
        presents=Count('attendance', filter=Q(attendance__status='Present')),
        absents=Count('attendance', filter=Q(attendance__status='Absent'))
    )

    # Chart uchun data
    chart_students = [s.user.username for s in report_data]
    chart_presents = [s.presents for s in report_data]
    chart_absents = [s.absents for s in report_data]

    return render(request, 'attendance/report.html', {
        'report_data': report_data,
        'chart_students': chart_students,
        'chart_presents': chart_presents,
        'chart_absents': chart_absents
    })

# Signup
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'attendance/signup.html', {'error': "Passwords do not match"})

        if User.objects.filter(username=username).exists():
            return render(request, 'attendance/signup.html', {'error': "Username already exists"})

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        return redirect('dashboard')

    return render(request, 'attendance/signup.html')

# Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'attendance/login.html', {'error': "Invalid username or password"})

    return render(request, 'attendance/login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')


# Add Student (Teacher)
@login_required
def add_student(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        roll_number = request.POST['roll_number']
        department = request.POST['department']

        # User ham yaratish (student uchun login uchun)
        username = f"{first_name.lower()}.{last_name.lower()}"
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password='123456')  # default password
        else:
            user = User.objects.get(username=username)

        Student.objects.create(
            user=user,
            roll_number=roll_number,
            department=department
        )
        return redirect('dashboard')

    return render(request, 'attendance/add_student.html')
