from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
import os
from .utils import create_docx

def upload_pdf(request):
    if request.method == "POST":
        output_path = os.path.join(
            settings.MEDIA_ROOT, "output", "mediation_form.docx"
        )
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        create_docx(output_path)

        return FileResponse(
            open(output_path, 'rb'),
            as_attachment=True,
            filename="mediation_form.docx"
        )

    return render(request, "upload.html")
