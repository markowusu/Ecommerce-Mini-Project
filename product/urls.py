from django.urls import path, include 

from . import views

urlpatterns =[
    path('latest-product/', views.LatestProductList.as_view()),
    path('product/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetails.as_view())
]