from typing import Type
from django.db.models import NOT_PROVIDED
from rest_framework import serializers

from .models.base import BaseModel


def get_model_serializer(
    data_model: Type[BaseModel]
) -> Type[serializers.ModelSerializer]:
    """
    Generate a serializer class for a given model.
    """

    class ModelSerializer(serializers.ModelSerializer[BaseModel]):
        class Meta:
            model = data_model
            fields = "__all__"

    return ModelSerializer
