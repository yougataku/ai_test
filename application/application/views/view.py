from django.shortcuts import render, redirect
from .forms import ContactForm
from application.models import Contact
from rest_framework.decorators import api_view

@api_view(["GET", "POST"])
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})