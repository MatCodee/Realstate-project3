from django.shortcuts import render
from django.core.mail import send_mail
from app import settings
# models:
from .models import Property,AdditionalImage
from blog.models import Blog
# forms
from .forms import ContactForm

def HomeView(request):  
    context = {}
    properties = Property.objects.all()
    context['properties'] = properties
    context['blogs'] = Blog.objects.all()
    return render(request,"home/home.html",context)

def AboutView(request):
    return render(request,"about/about.html",{})

def ServicesView(request):
    return render(request,"services/services.html",{})

def ContactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'Nuevo mensaje de contacto'
            content = f'Nombre: {fullname}\nTeléfono: {phone}\nCorreo electrónico: {email}\nMensaje: {message}'
            send_mail(subject, content, settings.EMAIL_HOST_USER, ['matias.altamiranove@gmail.com'], fail_silently=False)
            
            # Redireccionar a una página de éxito o mostrar un mensaje de éxito
            return render(request, 'status/success.html',{})
    else:
        form = ContactForm()
    return render(request,"contact/contact.html",{'form': form})


from user_act.models import CompanyMember
def TeamView(request):
    context = {}
    company_members = CompanyMember.objects.all()
    context['members'] = company_members
    return render(request,"team/team.html",context)


def PropertyView(request):
    context = {}
    properties = Property.objects.all()
    context['properties'] = properties
    return render(request,"propertie/properties.html",context)


def DetailPropertyView(request,id):
    context = {}
    property = Property.objects.get(pk=id)
    context['property'] = property
    context['images'] = AdditionalImage.objects.filter(property=property)
    return render(request,"propertie/detail_property.html",context)
