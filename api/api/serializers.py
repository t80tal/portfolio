from typing import Type

from django.db.models import NOT_PROVIDED
from rest_framework import serializers

from .models.base import BaseModel


def get_model_serializer(
    data_model: Type[BaseModel],
    model_fields: list[str] | str | None = None,
    name_suffix: str | None = None
) -> Type[serializers.ModelSerializer]:
    """
    Generate a serializer class for a given model.
    """

    if (isinstance(model_fields, str) and model_fields == "__all__" or
            model_fields is None):
        model_fields = [field.name for field in data_model._meta.fields]

    class ModelSerializer(serializers.ModelSerializer[BaseModel]):
        class Meta:
            model = data_model
            fields = model_fields or "__all__"

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                model_field = data_model._meta.get_field(field_name)
                is_nullable = (getattr(model_field, "null", False) and
                               getattr(model_field, "blank", False))
                if is_nullable:
                    field.required = False
                    field.allow_null = True
                default_value = getattr(model_field, "default", None)
                if default_value and default_value != NOT_PROVIDED:
                    field.default = (default_value() if callable(default_value)
                                     else default_value)
                    field.required = False

            ModelSerializer.__name__ = (
                f"{data_model.__name__}{name_suffix or ''}Serializer"
            )

    return ModelSerializer
