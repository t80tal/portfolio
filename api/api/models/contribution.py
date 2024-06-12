from django.db import models

from .base import BaseModel

class Contribution(BaseModel):
    repository_link = models.CharField(max_length=255)
