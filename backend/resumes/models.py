from django.db import models

class Resume(models.Model):
    file = models.FileField(upload_to="resumes/")
    original_name = models.CharField(max_length=255)

    parsed_text = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_name
