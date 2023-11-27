from django.test import TestCase
from django.urls import reverse,resolve

from shopee.views import allproducts



# Create your tests here.
class TestURL(TestCase):
    def test_urlhome(self):
        url=reverse("product_by_category",args=['demo_slug'])
        print("url is :",url)
        print("resolve:",resolve(url))
        self.assertEqual(resolve(url).func,allproducts)
