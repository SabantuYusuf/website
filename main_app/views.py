from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'About.html')


def project(request):
    return render(request, 'project.html')


# def contact(request):
#     name=''
#     email=''
#     comment=''
#     form= ContactForm(request.POST or None)
#     if form.is_valid():
#         name=form.cleaned_data.get('name')
#         email=form.cleanee_data.get('email')
#         comment=form.cleaned_data.get('comment')

#         if request.user.is_authenticated():
#             subject= str(request.user) + 's Comment'
#         else:
#             subject= "'A Visitor's Comment"

#             comment= name + 'with the email,' + email + ", sent the following message:\n\n" + comment;
#             send_mail(subject, comment, 'sabantuyusuf@gmail.com', [email])

#             context = {'form': form}
            
#             return render(request, 'contact.html', context)

#         else:
#             context={'form': form}
#             ruturn render(request, 'contact.html', context)


def contact(request):
    name=''
    email=''
    comment=''


    form= ContactForm(request.POST or None)
    if form.is_valid():
        name= form.cleaned_data.get("name")
        email= form.cleaned_data.get("email")
        comment=form.cleaned_data.get("comment")

        if request.user.is_authenticated:
            subject= str(request.user) + "'s Comment"
        else:
            subject= "A Visitor's Comment"


        comment= name + " with the email, " + email + ", sent the following message:\n\n" + comment;
        send_mail(subject, comment, email, ['sabantu.u@gmail.com'])


        context= {'form': form}

        return render(request, 'contact.html', context)

    else:
        context= {'form': form}
        return render(request, 'contact.html', context)

# def successView(request):
#     return HttpResponse('Success! Thank you for your message.')


