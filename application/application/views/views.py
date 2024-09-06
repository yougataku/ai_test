from django.shortcuts import render
import os
from django.conf import settings


def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        # uploaded_file = request.FILES['file']
        # # Process the uploaded file as needed
        # # For example, you can save it to a specific location
        # file_path = f'uploads/{uploaded_file.name}'
        # with open(file_path, 'wb+') as destination:
        #     for chunk in uploaded_file.chunks():
        #         destination.write(chunk)
        uploaded_file = request.FILES['file']
        # Construct the file path using the os module
        uploads_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
        os.makedirs(uploads_dir, exist_ok=True)  # Create the uploads directory if it doesn't exist
        file_path = os.path.join(uploads_dir, uploaded_file.name)

        # Save the uploaded file
        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # with open(file_path, 'r') as file:
        #     file_content = file.read()

        return render(request, 'display_file.html', {'file_path': file_path})
    else:
        return render(request, 'upload_file.html')
