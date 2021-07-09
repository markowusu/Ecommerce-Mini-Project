from django.core.management.base import BaseCommand
import pandas as pd 
from product.models import  Product,Category
import re

class Command(BaseCommand):
    help = "load data"

    def handle(self , *args, **options ):
        df = pd.read_csv("ecommerce.csv")
        # category = df.category.unique()

        # for CATEGORY  in zip(df.category.unique().tolist(), df[]:
        #     # print(CATEGORY)
        #     # print( CATEGORY.replace(" ", "-").lower())
        #     # models = Category(name=CATEGORY,slug=( CATEGORY.replace(" ", "-").lower()))
        #     models.save()

#         for SKU,PRODUCT_DESCRIPTION,PRODUCT_TAGS,IMAGE_URL,CATEGORY,PRODUCT_PRICE, PRODUCT_BRAND, PRODUCT_NAME in zip(df['Sku'],df['Product Description'],df['Product Tags'],df['Product Image Url'],df.category.unique().tolist(),df['Product Price'],df['Product Brand'],df['Product Name'].unique().tolist()):
#             print(CATEGORY)
# #             
#             models_cat = Category(name=CATEGORY,slug=( CATEGORY.replace(" ", "-").lower()))
#             models = Product(sku = SKU, description = PRODUCT_DESCRIPTION,meta_description=PRODUCT_TAGS,brand=PRODUCT_BRAND,price=PRODUCT_PRICE,name=PRODUCT_NAME,image_url = IMAGE_URL,slug=(PRODUCT_NAME.replace(" ","-").lower()), quantity =100)
#             models_cat.save()
#             models.categories = models_cat
#             models.save()
# # #

        for PRODUCT_NAME, PRODUCT_CONTENT in zip(df['Product Name'], df['Product Contents']):
            print(PRODUCT_NAME)
            try:
                models = Product.objects.get(name = PRODUCT_NAME)
                models.product_content = PRODUCT_CONTENT 
                models.save()
            except:
                continue
           
            
