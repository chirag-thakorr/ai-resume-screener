from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .skill_extractor import extract_skills


from .models import Resume
from .parser import extract_text_from_pdf


class ResumeUploadAPI(APIView):

    def post(self, request):
        if "file" not in request.FILES:
            return Response(
                {"error": "file required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        file = request.FILES["file"]

        resume = Resume.objects.create(
            file=file,
            original_name=file.name
        )

        text = extract_text_from_pdf(resume.file.path)
        skills = extract_skills(text)
        resume.parsed_text = text
        resume.skills = skills
        resume.save()

        return Response({
            "id": resume.id,
            "name": resume.original_name,
            "skills": skills,
            "skill_count": len(skills),
            "text_length": len(text)
        })

