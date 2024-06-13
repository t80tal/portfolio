from .crud_mixin import CRUDMixin
from rest_framework.test import APITestCase


class ContributionTests(CRUDMixin, APITestCase):
    endpoint = "/contribution/"
    dummy_1 = {
        "name": "Test Project",
        "description": "Test Description",
        "repository_link": "https://www.example.com",
    }
    dummy_2 = {
        "name": "Test Project2",
        "description": "Test Description2",
        "repository_link": "https://www.example.com",
    }
