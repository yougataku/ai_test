from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # ... (e.g., send an email, save to database)
            return redirect('success', name=name, email=email)
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def success(request, name, email):
    return render(request, 'success.html', {'name': name, 'email': email})
