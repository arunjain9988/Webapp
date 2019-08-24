from django.shortcuts import render

# Create your views here.
def machines(request):
    return render(request,'machines.html')


def spare_parts(request):
    return render(request,'spare_parts.html')


def repaires(request):
    return render(request,'repaires.html')
