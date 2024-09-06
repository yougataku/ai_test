from django.shortcuts import render, redirect
from .forms import RegistrationForm
from application.models import Registration
from django.urls import reverse

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('registered_users')) # Replace 'success_url' with the URL name you want to redirect to
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def registered_users_view(request):
    registered_users = Registration.objects.all()
    context = {'registered_users': registered_users}
    return render(request, 'registered_users.html', context)