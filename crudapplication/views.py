from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from crudapplication.forms import EmployeeForm
from crudapplication.models import Employee

# Create your views here.
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show/')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, "crudapplication/index.html", {'form': form})


def show(request):
    employees = Employee.objects.all()
    return render(request, 'crudapplication/show.html', {'employees': employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'crudapplication/edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'crudapplication/edit.html', {'employee': employee})

def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')