from django.shortcuts import render
from .models import EmployeeDetails
from .forms import DetailForm
from django.http import HttpResponse

# Create your views here.

def emp_create(request):
    form = DetailForm()
    if request.method == 'POST':
        form = DetailForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            return HttpResponse(f'Employee {name} is created')
    return render(request, 'create.html', {'form': form})


def emp_read(request, pk):
    data = EmployeeDetails.objects.get(id = pk)
    return render(request, 'read.html', {'data':data})


def emp_update(request, pk):
    data = EmployeeDetails.objects.get(id = pk)
    form = DetailForm(instance=data)
    if request.method == 'POST':
        form = DetailForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponse("Employee data is updated")
    return render(request, "update.html", {'form': form})

def emp_delete(request, pk):
    del_data = EmployeeDetails.objects.get(id = pk).delete()
    return HttpResponse('Employee Details are removed from Database')
