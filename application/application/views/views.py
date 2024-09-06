# views.py
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def process_form(request):
    if request.method == 'POST':
        # Get the form data from the request
        form_data = request.POST

        # Process the form data
        name = form_data.get('name', '')

        # Perform any necessary validation or processing
        if not name:
            error_message = 'Name is required'
            return render(request, 'error.html', {'error_message': error_message})

        # Construct the data to pass to the template
        result_data = {
            'message': f'Hello, {name}! Your form has been submitted successfully.',
            'status': 'success'

        }

        # Render the result template with the data
        return JsonResponse(result_data)
    else:
        return JsonResponse({'message': '無効なリクエスト', 'status': 'error'})



def form(request):
    return render(request, 'process_form.html')
