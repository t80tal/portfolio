from django.db import models

from .base import BaseModel

class Project(BaseModel):
    project_link = models.CharField(max_length=255)
    image_link = models.CharField(null=False, blank=False, max_length=255)
