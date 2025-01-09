from django.db import models

# Create your models here.
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ckeditor_upload(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        uploaded_file = request.FILES['upload']
        fs = FileSystemStorage(location='media/uploads/')
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)

        # Respond with the image URL, which CKEditor will use to display it
        return JsonResponse({
            'uploaded': True,
            'fileName': filename,
            'url': file_url
        })
    else:
        return JsonResponse({'uploaded': False})
