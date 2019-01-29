from .models import Product 


class ProductCrud():

  @classmethod
  def get_all_products(self):
    return Product.objects.all()