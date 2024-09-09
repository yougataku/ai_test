from django.shortcuts import render, redirect
from application.views.form import ContactForm
from rest_framework.decorators import api_view

@api_view(["GET","POST"])
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            
            # Redirect to a success view and pass the form data
            return redirect('success', name=name, email=email)

    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def success(request, name, email):
    return render(request, 'success.html', {'name': name, 'email': email})
