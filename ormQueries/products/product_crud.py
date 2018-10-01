from .models import Product 


class ProductCrud():

  @classmethod
  def get_all_products(self):
    
  @classmethod 
  def find_by_model(self, model):
     
  @classmethod
  def last_record(self):
    
  @classmethod 
  def by_rating(self, rating):
    
  @classmethod
  def by_rating_range(self, rating_min, rating_max):
      
  @classmethod
  def by_rating_and_color(self, rating, color):
    
  @classmethod
  def by_rating_or_color(self, rating, color):

  @classmethod
  def no_color_count(self):
    
  @classmethod
  def below_price_or_above_rating(self, price, rating):

  @classmethod
  def ordered_by_category_alpha_price_decending(self):

  @classmethod
  def products_by_manufacturer(self, name):

  @classmethod
  def manufacturer_names_for_query(self, name):
   
  @classmethod
  def not_in_a_category(self, category):

  @classmethod 
  def limited_not_in_a_category(self, category, limit):

  @classmethod
  def category_manufacturers(self, category):
  
  @classmethod 
  def average_category_rating(self, category):
    
  @classmethod 
  def greatest_price(self):
  @classmethod 
  def ordered_by_model_length(self):
    
  @classmethod
  def longest_model_name(self):
