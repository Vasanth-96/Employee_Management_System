from datetime import datetime
import imp
from django.db.models import Q
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from .models import Role, Employee, Department
# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def all_emp(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'all_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name= first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id = dept, role_id = role, hire_date = datetime.now() )
        new_emp.save()
        return HttpResponse('Employee added Successfully')
    elif request.method=='GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An Exception Occured! Employee Has Not Been Added")

def del_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('Employee Removed sucessfully')
        except:
            return HttpResponse('Enter a vaild Employee Id')
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'del_emp.html', context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        salary=request.POST['salary']
        employees = Employee.objects.all()
        if name:
            employees = employees.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            employees = employees.filter(dept__name__icontains = dept)
        if role:
            employees = employees.filter(role__name__icontains = role)
        if salary:
            employees = employees.filter(salary__icontains = salary)
        context = {
            'employees': employees
        }
        return render(request, 'all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')


