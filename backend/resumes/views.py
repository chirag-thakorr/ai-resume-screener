from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Resume
from .serializers import ResumeSerializer
from .parser import extract_text_from_pdf


class ResumeUploadAPI(APIView):

    def post(self, request):
        file = request.FILES["file"]

        resume = Resume.objects.create(
            file=file,
            original_name=file.name
        )

        text = extract_text_from_pdf(resume.file.path)
        resume.parsed_text = text
        resume.save()

        return Response({
            "id": resume.id,
            "name": resume.original_name,
            "chars": len(text)
        })
