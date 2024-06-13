from rest_framework import status
from django.contrib.auth import get_user_model


class CRUDMixin:
    endpoint = None
    dummy_1 = {}
    dummy_2 = {}

    def setUp(self):
        self.client = self.client_class()
        self.user = get_user_model().objects.create_superuser(
            username='testuser',
            password='testpassword'
        )
        if not self.endpoint:
            raise ValueError("Endpoint not set")
        if not self.dummy_1:
            raise ValueError("Dummy 1 not set")
        if not self.dummy_2:
            raise ValueError("Dummy 2 not set")

    def authenticate(self):
        self.client.force_authenticate(self.user)

    def logout(self):
        self.client.logout()

    def create_instance(self):
        response = self.client.post(self.endpoint, data=self.dummy_1)
        return response

    def test_create_instance(self):
        response = self.create_instance()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.authenticate()
        response = self.create_instance()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_instance(self):
        self.authenticate()
        response = self.create_instance()
        self.logout()

        instance_id = response.data['id']
        response = self.client.get(f"{self.endpoint}{instance_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_instance(self):
        self.authenticate()
        response = self.create_instance()
        self.logout()

        instance_id = response.data['id']
        response = self.client.patch(
            f"{self.endpoint}{instance_id}/", data=self.dummy_2
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.authenticate()
        response = self.client.patch(
            f"{self.endpoint}{instance_id}/", data=self.dummy_2
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_instance(self):
        self.authenticate()
        response = self.create_instance()
        self.logout()

        instance_id = response.data['id']
        response = self.client.delete(f"{self.endpoint}{instance_id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.authenticate()
        response = self.client.delete(f"{self.endpoint}{instance_id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
