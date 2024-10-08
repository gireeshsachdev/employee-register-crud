from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)
 
def employee_form(request, id=0): # Will use this for INSERT & UPDATE an EMPLOYEE
    if request.method == "GET":
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/employee/list')


def employee_delete(request, id): # Will use this to DELETE an EMPLOYEE
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect ('/employee/list')