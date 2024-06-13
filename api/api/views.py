from typing import Type, cast
from django.urls import URLPattern, URLResolver
from rest_framework import viewsets
from rest_framework.routers import SimpleRouter
from rest_framework.permissions import IsAuthenticated

from .models.base import BaseModel
from .serializers import get_model_serializer


def get_urls(model: Type[BaseModel]) -> list[URLPattern | URLResolver]:
    """
    Generate a list of URL patterns for a given model.
    """
    url_path_segment = model._meta.db_table.replace("_", "-")
    model_serializer = get_model_serializer(model)

    class ModelViewSet(viewsets.ModelViewSet):
        queryset = model.objects.order_by("-created_at")
        serializer_class = model_serializer

        def get_permissions(self):
            """
            Instantiates and returns the list of permissions.
            """
            if not self.request.method == 'GET':
                self.permission_classes = [IsAuthenticated]
            return super().get_permissions()

    router = SimpleRouter()
    router.register(url_path_segment, ModelViewSet)

    return router.urls


urls = [
    url for model in BaseModel.__subclasses__()
    for url in get_urls(cast(Type[BaseModel], model))
]
