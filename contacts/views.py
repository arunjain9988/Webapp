from django.shortcuts import render,get_object_or_404
from .models import Organization,Contact
# Create your views here.
def add_contact(request):
    if(request.GET):
        contact = Contact()
        contact.fname=request.GET['fname']
        contact.lname=request.GET['lname']
        contact.email=request.GET['pemail']
        contact.mobile=request.GET['mobile']
        contact.address=request.GET['address']
        contact.city=request.GET['city']
        org_id = request.GET['org']
        org = get_object_or_404(Organization,pk=org_id)
        contact.company=org
        contact.save()
        return render(request,'file.html')
    organizations = Organization.objects
    return render(request,'add_contact.html',{'organizations':organizations})


def add_organization(request):
    if(request.GET):
        org = Organization()
        org.name=request.GET['name']
        org.gst_no=request.GET['gstno']
        org.primary_phone=request.GET['pphone']
        org.secondary_phone=request.GET['sphone']
        org.primary_email=request.GET['pemail']
        org.secondary_email=request.GET['semail']
        org.address=request.GET['address']
        org.city=request.GET['city']
        org.state=request.GET['state']
        org.country=request.GET['country']
        org.save()
        return render(request,'file.html')
    return render(request,'add_organization.html')


def index(request):
    return render(request,'index.html')

def contacts(request):
    contacts = Contact.objects
    return render(request,'contacts.html',{'contacts':contacts})

def organizations(request):
    organizations = Organization.objects
    return render(request,'organizations.html',{'organizations':organizations})

def contact_profile(request,contact_id):
    contact = get_object_or_404(Contact,pk=contact_id)
    return render(request,'contact_profile.html',{'contact':contact})

def organization_profile(request,organization_id):
    organization = get_object_or_404(Organization,pk=organization_id)
    return render(request,'organization_profile.html',{'organization':organization})
