from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse

# Create your views here.
def contact(request):
    contactForm=ContactForm()#crea instancia
    #instanciar la clase del formulario
    #print("Tipo de peticion: {}".format(request.method))
    if request.method=="POST":
       contactForm=ContactForm(data=request.POST)
       if contactForm.is_valid():
           name = request.POST.get('name','')
           email = request.POST.get('email','')
           content = request.POST.get('content','')
           #enviar correo
           email=EmailMessage(
             "La Caffettiera: Nuevo mensaje de contacto",    #asunto
             "De {} <{}>\n\nEscribio:\n\n{}".format(name,email,content),  #cuerpo
             "no-contestar@inbox.mailtrap.io", # email_origen
             ["luis.perdomo@hotmail.com"],  # email_destino
             reply_to=[email]
           )
           try:
               email.send()
               return redirect(reverse('contact')+"?ok")
           except:
               return redirect(reverse('contact')+"?fail")
          
    return render(request, "contact/contact.html", {'form':contactForm})
