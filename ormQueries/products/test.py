from django.test import TestCase
from .models import Product 
from .product_crud import ProductCrud

class ProductCrudTestCase(TestCase):
  
  def test_get_all_products(self):
    self.assertQuerysetEqual(ProductCrud.get_all_products(), Product.objects.all())