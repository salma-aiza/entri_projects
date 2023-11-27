from django.test import TestCase,Client
from django.urls import reverse,resolve


class testviewhome(TestCase):
    def test_home(self):
        client=Client()
        response=client.get(reverse('allproducts'))
        print("response",response)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'tem1.html')
