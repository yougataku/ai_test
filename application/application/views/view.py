from django.shortcuts import render, redirect
from application.views.form import ContactForm
from rest_framework.decorators import api_view

@api_view(["GET"])
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})