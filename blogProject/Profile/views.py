from django.shortcuts import render, redirect
from .models import Contact, About, FAQ
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.

def contact(request):
    """ contact us view """
    contact_info = Contact.objects.first()
    
    context = {
        "contact_info": contact_info
    }
    return render(request, 'contact.html', context)

def about(request):
    """ about us view """
    contact_info = Contact.objects.first()
    about_info = About.objects.first()  # Use a different variable name to avoid conflict
    faqs = FAQ.objects.all()
    
    context = {
        "contact_info": contact_info,
        "about_info": about_info,  # Update the context variable name
        "faqs": faqs,
    }
    return render(request, 'about.html', context)

def log_in(request):
    """ Login view """
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page or home page
            messages.success(request, 'login successful')
            return redirect('home')  # Assuming you have a URL pattern named 'home'
        else:
            # Authentication failed, display an error message
           messages.error(request, "username and/or password incorrect")

    return render(request, 'login.html')

def log_out(request):
    """ Logout view """
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home') 
