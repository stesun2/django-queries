from .models import Product 
from django.db.models import Q, Avg, Max
from django.db.models.functions import Length


class ProductCrud():

  @classmethod
  def get_all_products(self):
    return Product.objects.all()

  @classmethod 
  def find_by_model(self, model):
    return Product.objects.get(model=model)
     
  @classmethod
  def last_record(self):
    return Product.objects.last()
  @classmethod 
  def by_rating(self, rating):
    return Product.objects.filter(rating=rating)
  
  @classmethod
  def by_rating_range(self, rating_min, rating_max):
    return Product.objects.filter(rating__range=(rating_min, rating_max))
    
  @classmethod
  def by_rating_and_color(self, rating, color):
    return Product.objects.filter(rating=rating, color=color)
  
  @classmethod
  def by_rating_or_color(self, rating, color):
    return Product.objects.filter(Q(rating=rating) | Q(color=color))

  @classmethod
  def no_color_count(self):
    return Product.objects.filter(color=None).count()
    
  @classmethod
  def below_price_or_above_rating(self, price, rating):
    return Product.objects.filter(Q(price_cents__lt=price) | Q(rating__gt=rating))

  @classmethod
  def ordered_by_category_alpha_price_decending(self):
    return Product.objects.order_by('category', '-price_cents')

  @classmethod
  def products_by_manufacturer(self, name):
    return Product.objects.filter(manufacturer__contains=name)

  @classmethod
  def manufacturer_names_for_query(self, name):
    query = Product.objects.filter(manufacturer__contains=name)
    return list(query.values_list('manufacturer', flat=True))
  
  @classmethod
  def not_in_a_category(self, category):
    return Product.objects.exclude(category=category)

  @classmethod 
  def limited_not_in_a_category(self, category, limit):
    return Product.objects.exclude(category=category)[:limit]

  @classmethod
  def category_manufacturers(self, category):
    products = Product.objects.filter(category=category)
    return list(products.values_list('manufacturer', flat=True))
  
  @classmethod 
  def average_category_rating(self, category):
    return Product.objects.filter(category=category).aggregate(Avg('rating'))
    
  @classmethod 
  def greatest_price(self):
    return Product.objects.all().aggregate(Max('price_cents'))
  @classmethod 
  def ordered_by_model_length(self):
    return Product.objects.annotate(text_len=Length('model')).order_by('text_len')
    
  @classmethod
  def longest_model_name(self):
    return Product.objects.annotate(text_len=Length('model')).order_by('-text_len')[0].text_len
