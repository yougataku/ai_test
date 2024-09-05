from django.shortcuts import render, redirect
from .forms import SampleForm

def sample_view(request):
    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            
            # Redirect to a success view and pass the form data
            return redirect('success', name=name, email=email)
    else:
        form = SampleForm()
    
    return render(request, 'sample_template.html', {'form': form})

def success(request, name, email):
    return render(request, 'success.html', {'name': name, 'email': email})

