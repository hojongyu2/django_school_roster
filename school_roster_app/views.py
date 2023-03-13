from django.shortcuts import render
# Create your views here.
# school_roster_app/views.py

from django.shortcuts import render
from .models import School # import our School class

my_school = School("Django School") # create a school instance


def index(request):
    my_data = { 
        "school_name": my_school.name
    }
    return render(request, "pages/index.html", my_data)


def list_staff(request):
    my_data = {
        "staff": my_school.staff
    }
    return render(request, "pages/staff.html", my_data)

def staff_detail(request, employee_id):
    my_data = {
        "staff_member": my_school.find_staff_by_id(employee_id)
    }
    return render(request, 'pages/staff.html', my_data)

def list_students(request):
    my_data = {
        "students": my_school.students
    }
    return render(request, "pages/students.html", my_data)


def student_detail(request, student_id):
    my_data = {
        "students_by_id" : my_school.find_student_by_id(student_id)
    }
    return render(request, "pages/students.html", my_data)