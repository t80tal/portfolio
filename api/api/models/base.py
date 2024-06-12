from django.db import models
import re

class BaseModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=False, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.Meta.db_table = re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower()
