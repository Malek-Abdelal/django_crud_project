from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Snack
from django.urls import reverse

# Create your tests here.

class SnackTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='user',email='user@user.com',
            password='user@12345'
        )

        self.snack = Snack.objects.create(
            title = 'test',
            purchaser = self.user,
            description = 'description'
        )

    def test_str_method(self):
        self.assertEqual(str(self.snack),'test')

    def test_detail(self):
        url = reverse('snack_details', args = [self.snack.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_details.html')

    def test_create(self):
        url = reverse('create_snack')
        data = {
            "title": "test1",
            "purchaser" : self.user.id,
            "description": 'description'
        }
        response = self.client.post(path = url, data = data, follow = True)
        self.assertTemplateUsed(response,'snack_details.html')
        self.assertEqual(len(Snack.objects.all()),2)
        self.assertRedirects(response, reverse('snack_details',args=[2]))

    def test_update(self):
        url = reverse('update_snack', args = [self.snack.id])
        data = {
            "title": "updated_test",
            "purchaser": self.user.id,
            "description": 'updated_description'
        }
        response = self.client.post(path=url, data=data, follow=True)
        self.assertTemplateUsed(response, 'snacks_list.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Snack.objects.get(id=self.snack.id).title, 'updated_test')

    def test_delete(self):
        url = reverse('delete_snack', args = [self.snack.id])
        response = self.client.post(path = url, follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Snack.objects.all()), 0)
        self.assertRedirects(response, reverse('snacks')) 
