from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            
            # Redirect to a success view and pass the form data
            return redirect('success', name=name, email=email)
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def success(request, name, email):
    return render(request, 'success.html', {'name': name, 'email': email})
