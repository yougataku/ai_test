from django.shortcuts import render

def home(request):
    # Logic for the home view
    return render(request, 'home.html')

def contact(request):
    # Logic for the contact view
    return render(request, 'contact.html')

def service(request):
    # Logic for the service view
    return render(request, 'service.html')