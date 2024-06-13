from .crud_mixin import CRUDMixin
from rest_framework.test import APITestCase


class ProjectTests(CRUDMixin, APITestCase):
    endpoint = "/project/"
    dummy_1 = {
        "name": "Test Project",
        "description": "Test Description",
        "project_link": "https://www.example.com",
        "image_link": "https://www.example.com",
    }
    dummy_2 = {
        "name": "Test Project2",
        "description": "Test Description2",
        "project_link": "https://www.example2.com",
        "image_link": "https://www.example2.com",
    }
