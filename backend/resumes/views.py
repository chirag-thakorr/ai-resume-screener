from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .scripts.skill_extractor import extract_skills
from .models import Resume, JobDescription
from .scripts.parser import extract_text_from_pdf
from .serializers import JDSerializer
from .scripts.matcher import skill_match_score, combined_score


class MatchAPI(APIView):

    def get(self, request, jd_id):

        jd = JobDescription.objects.get(id=jd_id)
        resumes = Resume.objects.all()

        results = []

        for r in resumes:
            # score, matched = skill_match_score(jd.skills, r.skills)
            score, matched, sem = combined_score(jd, r)

            results.append({
                "resume_id": r.id,
                "name": r.original_name,
                "final_score": score,
                "skill_score": len(matched),
                "semantic_score": sem,
                "matched_skills": matched
            })
            # results.append({
            #     "resume_id": r.id,
            #     "name": r.original_name,
            #     "score": score,
            #     "matched_skills": matched
            # })

        results.sort(key=lambda x: x["final_score"], reverse=True)

        return Response(results)



class JDCreateAPI(APIView):

    def post(self, request):
        title = request.data.get("title")
        text = request.data.get("text")

        skills = extract_skills(text)

        jd = JobDescription.objects.create(
            title=title,
            text=text,
            skills=skills
        )

        return Response({
            "id": jd.id,
            "title": jd.title,
            "skills": skills
        })




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

