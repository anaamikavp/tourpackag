from django.shortcuts import render
from vendor.models import package_table

# Create your views here.
def admin_index(request):
    return render(request,'admin_index.html')

def admin_packages(request):
    package_data = package_table.objects.all()
    return render(request,'admin_view_packages.html',{'pdata':package_data})

def package_details(request,id):
    package_data = package_table.objects.get(id=id)
    return render(request,'package_details.html',{'pdata':package_data})

def approve_package(request, id):
    package_data = package_table.objects.get(id=id)
    package_data.status = "approved"
    package_data.save()
    return render(request,'package_details.html',{'pdata':package_data})

def reject_package(request, id):
    package_data = package_table.objects.get(id=id)
    package_data.status = "rejected"
    package_data.save()
    return render(request,'package_details.html',{'pdata':package_data})
